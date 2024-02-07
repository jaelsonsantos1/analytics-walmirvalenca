import streamlit as st
from controllers.colaborador_controller import ColaboradorController as cc

# configurações da página
st.set_page_config(
    page_title="Cadastro de Colaboradores",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Obter todos os gestores e setores
gestores_lista = cc.get_all_gestores()
setores_lista = cc.get_all_setores()

idAlteracao = st.experimental_get_query_params()
st.experimental_set_query_params()

# Defini o título da página com base no Id guardado em idAlteracao
if idAlteracao != {}:
    st.title('Alterar dados do colaborador')
else:
    st.title('Cadastrar novo colaborador')

#  Formulário
with st.form(key='form-cadastro', clear_on_submit=True):
    dadoRecuperado = None

    # Atualizar cadastro
    if idAlteracao != {}:
        idAlteracao = idAlteracao['id'][0]
        dadoRecuperado = cc.get_colaborador_by_id(idAlteracao)

        indice_gestor = [id for id, nome in gestores_lista].index(dadoRecuperado['id_gestor'][0])
        indice_setor = [id for id, nome in setores_lista].index(dadoRecuperado['id_setor'][0])

        st.experimental_set_query_params(
            id=[dadoRecuperado['id'][0]]
        )

        col1, col2 = st.columns(2)
        nome = col1.text_input('Nome', key='nome', help='Digite o nome do colaborador', max_chars=100, value=dadoRecuperado['nome'][0])
        idade = col2.number_input('Idade', key='idade', help='Digite a idade do colaborador', min_value=0, max_value=100, value=dadoRecuperado['idade'][0])
        gestor = col1.selectbox("Gestor", [nome for id, nome in gestores_lista], key="gestor", index=indice_gestor, help="Selecione o gestor")
        id_gestor_selecionado = [id for id, nome in gestores_lista if nome == gestor][0]
        setor = col2.selectbox("Alocação", [setor for id, setor in setores_lista], key="alocacao", index=indice_setor, help="Selecione a alocação")
        id_setor_selecionado = [id for id, nome in setores_lista if nome == setor][0]

        cols = col1.columns(4)
        btn_salvar = cols[0].form_submit_button('Alterar', on_click=None)
        btn_cancelar = cols[1].form_submit_button('Cancelar', on_click=None)
        
        if btn_salvar:
            if nome == '' or idade == 0 or gestor == '' or setor == '':
                st.error("Preencha todos os campos!")
            else:
                try:
                    colaborador_id = cc().update_colaborador(idAlteracao, nome, idade, id_gestor_selecionado, id_setor_selecionado)
                    st.success("Colaborador alterado com sucesso!")
                    st.experimental_set_query_params()
                    st.rerun()
                except Exception as e:
                    st.error("Erro ao alterar colaborador!")
                    st.error(e)
        elif btn_cancelar:
            st.experimental_set_query_params()
            st.rerun()

    # Cadastrar novo colaborador
    else:
        col1, col2 = st.columns(2)
        nome = col1.text_input('Nome', key='nome', help='Digite o nome do colaborador', max_chars=100)
        
        idade = col2.number_input('Idade', key='idade', help='Digite a idade do colaborador', min_value=0, max_value=70)
        
        nome_gestor_selecionado = col1.selectbox("Gestor", ['', *[nome for id, nome in gestores_lista]], key="gestor", index=0, help="Selecione o gestor")
        id_gestor_selecionado = [id for id, nome in gestores_lista if nome == nome_gestor_selecionado][0] if nome_gestor_selecionado != '' else None

        nome_setor_selecionado = col2.selectbox("Alocação", ['', *[nome for id, nome in setores_lista]], key="alocacao", index=0, help="Selecione a alocação")
        id_setor_selecionado = [id for id, nome in setores_lista if nome == nome_setor_selecionado][0] if nome_setor_selecionado != '' else None
        
        st.write("---")

        btn = st.form_submit_button('Cadastrar', on_click=None)

        if btn:
            if nome == '' or idade <= 18 or id_gestor_selecionado == None or id_setor_selecionado == None:
                st.error("Preencha todos os campos!")
            else:
                try:
                    print(nome, idade, id_gestor_selecionado, id_setor_selecionado)
                    cc().create_colaborador(nome, idade, id_gestor_selecionado, id_setor_selecionado)
                    st.success("Colaborador cadastrado com sucesso!")
                    st.experimental_set_query_params()
                except Exception as e:
                    st.error("Erro ao cadastrar colaborador!")
                    st.error(e)


paramId = st.experimental_get_query_params()
if paramId == {}:
    colaboradores_df = cc.get_all_colaboradores()
    if colaboradores_df is None or colaboradores_df.empty:
        st.warning("Nenhum colaborador encontrado")
    else:
        colaboradores_df = colaboradores_df[['id', 'nome', 'idade', 'id_gestor', 'gestor', 'id_setor', 'setor', 'created_at']]
        header_columns = ['Nome', 'Idade', 'Gestor', 'Alocação', 'Data/hora', 'Atualizar', 'Excluir']

        # Defina o número de itens por página
        itens_por_pagina = 5
        tot_pag = (len(colaboradores_df) - 1) // itens_por_pagina + 1
        pagina = st.sidebar.number_input(label='Página carregadas', min_value=1, max_value=tot_pag, value=1)
        # Mostrar a página atual/ total de páginas
        st.sidebar.write(f'Página {pagina} de {tot_pag}')

        inicio = (pagina - 1) * itens_por_pagina
        fim = pagina * itens_por_pagina
        
        # Crie as colunas na interface gráfica
        columns = st.columns(7)
        for col, header in zip(columns, header_columns):
            col.markdown(f'<p style="font-size: 20px; color: gray;border-bottom:2px solid #52cc72;padding-bottom:2px;">{header}</p>', unsafe_allow_html=True)
        
        colaboradores_pagina = colaboradores_df.iloc[inicio:fim, :]

        # Preencha a tabela com os dados da página selecionada
        for item in colaboradores_pagina.itertuples():
            columns = st.columns(7)
            columns[0].write(item.nome)
            columns[1].write(item.idade)
            columns[2].write(item.gestor)
            columns[3].write(item.setor)
            columns[4].write(item.created_at)
        
            # Btn update
            on_click_update = columns[5].button(":orange[Atualizar]", f'btnAtualizar-{item.Index}')
            #  implementar atualização
            if on_click_update:
                st.experimental_set_query_params(id=[item.id])
                st.rerun()

            # Btn delete
            on_click_delete = columns[6].button(":red[Excluir]", f'btnExcluir-{item.Index}')
            if on_click_delete:
                colaborador_id = cc.delete_colaborador(item.id)
                st.rerun()
