import streamlit as st
from controllers.desemepnho_controller import DesempenhoController as dc

# configurações da página
st.set_page_config(
    page_title="Dashboard Satisfação",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

desempenhos = dc.get_all_desempenhos()
st.sidebar.title('Menu')

st.title('Avaliação de Liderança - Desemepnho')

paramId = st.experimental_get_query_params()
if paramId == {}:
    
    colaborador_find = st.sidebar.selectbox('Selecione o colaborador', ['Todos', *desempenhos['nome_colaborador'].unique()])
    find_gestor = st.sidebar.selectbox('Selecione o gestor', ['Todos', *desempenhos['nome_gestor'].unique()])
    find_setor = st.sidebar.selectbox('Selecione o setor', ['Todos', *desempenhos['nome_setor'].unique()])

    if colaborador_find != 'Todos':
        desempenhos = desempenhos[desempenhos['nome_colaborador'] == colaborador_find]
    if find_gestor != 'Todos':
        desempenhos = desempenhos[desempenhos['nome_gestor'] == find_gestor]
    if find_setor != 'Todos':
        desempenhos = desempenhos[desempenhos['nome_setor'] == find_setor]

    header_columns = ['Colaborador', 'Avaliação', 'Gestor', 'Comentario', 'setor', 'Data/hora', 'Excluir']

    # Defina o número de itens por página
    itens_por_pagina = 10
    tot_pag = (len(desempenhos) - 1) // itens_por_pagina + 1
    col1, col2 = st.columns(2)
    if tot_pag == 0:
        tot_pag = 1
    pagina = col1.number_input(label='Página carregadas', min_value=1, max_value=tot_pag, value=1)
    st.write(f'Página {pagina} de {tot_pag}')
    # Mostrar a página atual/ total de páginas

    inicio = (pagina - 1) * itens_por_pagina
    fim = pagina * itens_por_pagina
    
    columns = st.columns(7)
    for col, header in zip(columns, header_columns):
        col.markdown(f'<p style="font-size: 20px; color: gray;border-bottom:2px solid grey;padding-bottom:2px;">{header}</p>', unsafe_allow_html=True)

    colaboradores_pagina = desempenhos.iloc[inicio:fim, :]

    for item in colaboradores_pagina.itertuples():
        columns = st.columns(7)
        columns[0].write(item.nome_colaborador)
        columns[1].write(item.nota_avaliacao)
        columns[2].write(item.nome_gestor)
        columns[3].write(item.comentario)
        columns[4].write(item.nome_setor)
        columns[5].write(item.created_at)

        # Btn delete
        on_click_delete = columns[6].button(":red[Excluir]", f'btnExcluir-{item.Index}')
        if on_click_delete:
            try:
                st.cache_resource.clear()
                dc().delete_desempenho(id=item.id)
                st.rerun()
            except Exception as e:
                st.error(f'Erro ao excluir o feedback: {e}')
