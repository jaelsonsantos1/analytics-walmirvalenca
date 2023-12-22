import streamlit as st
from controllers.colaborador_controller import ColaboradorController
from controllers.feedback_controller import FeedbackController

st.set_page_config(
    page_title="Dashboard Satisfação",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Registre aqui sua avaliação")
st.divider()

colaborador_df = ColaboradorController.get_all_colaboradores()
feedback_df = FeedbackController.get_all_feedbacks()

col1, col2 = st.columns(2)

# Inserindo um campo de avaliador
gestores_lista = sorted(['', 'Gilberto', 'Wellington', 'Joana', 'Joanir', 'Walmir', 'Alberto', 'Juvenal'])
gestor = col1.selectbox("Gestor", gestores_lista, key="gestor", index=0, help="Selecione o gestor")

# Inserindo um campo de colaborador
colaborador_nomes = sorted(list(colaborador_df['nome'].unique()), key=str.lower)
colaborador = col2.selectbox("Colaborador", colaborador_nomes, index=0, key="colaborador", help="Selecione o colaborador")

# Inseringo os campos para feedback
st.subheader("Feedback")

opcoes = [
    '👎 Desconectado',
    '😐 Insatisfeito',
    '👍 Conectado',
    '😍 Excepicional'
]
voto = st.radio("Como você avalia o colaborador?", opcoes, index=0, key="feedback")
voto = 1 if voto == "👎 Desconectado" else 2 if voto == "😐 Insatisfeito" else 3 if voto == "👍 Conectado" else 4

comments = st.text_area("Comentário", key="comment", height=100, max_chars=100, placeholder="Deixe aqui seu comentário")

btn = st.button("Enviar", key="register", help="Registra a avaliação no sistema", on_click=None)
if btn:
    if gestor == '':
        st.error("Selecione o gestor!")
    else:
        feedback = FeedbackController().create_feedback(gestor, colaborador, voto, comments)

        st.success("Avaliação registrada com sucesso!")
        st.balloons()
