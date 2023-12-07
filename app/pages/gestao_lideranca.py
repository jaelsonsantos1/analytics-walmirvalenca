import streamlit as st
from controllers.feedback_controller import FeedbackController

# configurações da página
st.set_page_config(
    page_title="Dashboard Satisfação",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# employees_df = ColaboradorController.get_all_colaboradores()
feedback_df = FeedbackController.get_all_feedbacks()
st.sidebar.title('Menu')

nome_gestores = feedback_df['gestor'].sort_values().unique()
nome_gestores = ['Todos'] + nome_gestores.tolist()
find_gestor =  st.sidebar.selectbox("Selecione o avaliador", nome_gestores, placeholder="Selecione o gestor")
find_gestor = find_gestor if find_gestor else "Sem informação"

st.title('Avaliação de Liderança')
st.subheader(f'Gestor: {find_gestor}')

paramId = st.experimental_get_query_params()
if paramId == {}:
    feedback_df = feedback_df[['id', 'gestor', 'nome', 'feedback', 'comentario', 'create_at']]
    feedback_df = feedback_df[feedback_df['gestor'] == find_gestor] if find_gestor != 'Todos' else feedback_df
    header_columns = ['Avaliado', 'Feedback', 'Comentario', 'Data/hora', 'Excluir']
    
    columns = st.columns(5)
    for col, header in zip(columns, header_columns):
        col.markdown(f'<p style="font-size: 20px; color: gray;border-bottom:2px solid grey;padding-bottom:2px;">{header}</p>', unsafe_allow_html=True)

    for item in feedback_df.itertuples():
        columns = st.columns(5)
        columns[0].write(item.nome)
        columns[1].write(item.feedback)
        columns[2].write(item.comentario)
        columns[3].write(item.create_at)
        
        # Btn delete
        on_click_delete = columns[4].button(":red[Excluir]", f'btnExcluir-{item.Index}')
        if on_click_delete:
            try:
                FeedbackController.delete_feedback(id=item.id)
                st.rerun()
            except Exception as e:
                st.error(f'Erro ao excluir o feedback: {e}')
