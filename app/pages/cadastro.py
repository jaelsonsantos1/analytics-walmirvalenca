import streamlit as st
from controllers import colaborador_controller as cc

# configurações da página
st.set_page_config(
    page_title="Cadastro de Colaboradores",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

idAlteracao = st.experimental_get_query_params()
st.experimental_set_query_params()

if idAlteracao != {}:
    st.title('Alterar dados do colaborador')
else:
    st.title('Cadastrar novo colaborador')

with st.form(key='form-cadastro', clear_on_submit=True):
    dadoRecuperado = None
    if idAlteracao != {}:
        idAlteracao = idAlteracao['id'][0]
        dadoRecuperado = cc.ColaboradorController.get_colaborador_by_id(idAlteracao)
        st.experimental_set_query_params(
            id=[dadoRecuperado['id'][0]]
        )

        col1, col2 = st.columns(2)
        gestores_lista = ['', 'Gilberto', 'Wellington', 'Joana', 'Joanir']
        alocacoes_lista = ['', 'Jurídico', 'Relacionamento', 'Santana', 'Financeiro', 'Administrativo', 'Itapipoca', 'Garanhuns']

        nome = col1.text_input('Nome', key='nome', help='Digite o nome do colaborador', max_chars=100, value=dadoRecuperado['nome'][0])
        idade = col2.number_input('Idade', key='idade', help='Digite a idade do colaborador', min_value=0, max_value=100, value=dadoRecuperado['idade'][0])
        gestor = col1.selectbox("Gestor", gestores_lista, key="gestor", index=gestores_lista.index(dadoRecuperado['gestor'][0]) , help="Selecione o gestor")
        alocacao = col2.selectbox("Alocação", alocacoes_lista, key="alocacao", index=alocacoes_lista.index(dadoRecuperado['alocacao'][0]), help="Selecione a alocação")
        btn = st.form_submit_button('Alterar', on_click=None)

        if btn:
            if nome == '' or idade == 0 or gestor == '' or alocacao == '':
                st.error("Preencha todos os campos!")
            else:
                try:
                    colaborador_controller = cc.ColaboradorController()
                    colaborador_id = colaborador_controller.update_colaborador(dadoRecuperado['id'][0], nome, idade, gestor, alocacao)
                    st.success("Colaborador alterado com sucesso!")
                    st.experimental_set_query_params()
                    st.rerun()
                except Exception as e:
                    st.error("Erro ao alterar colaborador!")
                    st.error(e)
                
    else:
        col1, col2 = st.columns(2)
        nome = col1.text_input('Nome', key='nome', help='Digite o nome do colaborador', max_chars=100)
        idade = col2.number_input('Idade', key='idade', help='Digite a idade do colaborador', min_value=0, max_value=100, value=0)
        gestor = col1.selectbox("Gestor", ['', 'Gilberto', 'Wellington', 'Joana', 'Joanir'], key="gestor", index=0, help="Selecione o gestor")
        alocacao = col2.selectbox("Alocação", ['', 'Jurídico', 'Relacionamento', 'Santana', 'Financeiro', 'Administrativo', 'Itapipoca', 'Garanhuns'], key="alocacao", index=0, help="Selecione a alocação")
        btn = st.form_submit_button('Cadastrar', on_click=None)

        if btn:
            if nome == '' or idade == 0 or gestor == '' or alocacao == '':
                st.error("Preencha todos os campos!")
            else:
                try:
                    colaborador_controller = cc.ColaboradorController()
                    colaborador_id = colaborador_controller.create_colaborador(nome, idade, gestor, alocacao)
                    st.success("Colaborador cadastrado com sucesso!")
                    st.experimental_set_query_params()
                except Exception as e:
                    st.error("Erro ao cadastrar colaborador!")
                    st.error(e)


paramId = st.experimental_get_query_params()
if paramId == {}:
    colaboradores_df = cc.ColaboradorController.get_all_colaboradores()
    colaboradores_df = colaboradores_df[['id', 'nome', 'idade', 'gestor', 'alocacao', 'create_at']]
    header_columns = ['Nome', 'Idade', 'Gestor', 'Alocação', 'Data/hora', 'Atualizar', 'Excluir']
    
    columns = st.columns(7)
    for col, header in zip(columns, header_columns):
        col.markdown(f'<p style="font-size: 20px; color: gray;border-bottom:2px solid #52cc72;padding-bottom:2px;">{header}</p>', unsafe_allow_html=True)

    for item in colaboradores_df.itertuples():
        columns = st.columns(7)
        columns[0].write(item.nome)
        columns[1].write(item.idade)
        columns[2].write(item.gestor)
        columns[3].write(item.alocacao)
        columns[4].write(item.create_at)
        
        # Btn update
        on_click_update = columns[5].button(":orange[Atualizar]", f'btnAtualizar-{item.Index}')
        #  implementar atualização
        if on_click_update:
            st.experimental_set_query_params(id=item.id)
            st.rerun()
 
        # Btn delete
        on_click_delete = columns[6].button(":red[Excluir]", f'btnExcluir-{item.Index}')
        if on_click_delete:
            colaborador_id = cc.ColaboradorController.delete_colaborador(item.id)
            st.rerun()
