import streamlit as st
from controllers.colaborador_controller import ColaboradorController
from controllers.feedback_controller import FeedbackController


# Configurações da página
st.set_page_config(
    page_title="Dashboard Satisfação",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Carrega os dados e armazena em cache
@st.cache_resource()
def loadData():
    colaborador_df = ColaboradorController.get_all_colaboradores()
    feedback_df = FeedbackController.get_all_feedbacks()
    return colaborador_df, feedback_df

colaborador_df, feedback_df = loadData()
gestores_lista = sorted(['', 'Gilberto', 'Wellington', 'Joana', 'Joanir', 'Walmir', 'Alberto', 'Juvenal'])
colaborador_nomes = sorted(list(colaborador_df['nome'].unique()), key=str.lower)
btn_voto_nulo = None

st.title("Registre aqui sua avaliação")

with st.form(key="form-avaliacao", clear_on_submit=True):
    col1, col2 = st.columns(2)
    gestor = col1.selectbox("Gestor", gestores_lista, key="gestor", index=0, help="Selecione o gestor")
    colaborador = col2.selectbox("Colaborador", colaborador_nomes, index=0, key="colaborador", help="Selecione o colaborador")
    opcoes = ['🙁 Desconectado', '😐 Insatisfeito', '🙂 Conectado', '🤩 Excepicional']
    voto = col1.radio("Como você avalia o colaborador?", opcoes, index=0, key="feedback")
    voto = 1 if voto == "🙁 Desconectado" else 2 if voto == "😐 Insatisfeito" else 3 if voto == "🙂 Conectado" else 4
    comments = st.text_area("Comentário", key="comment", height=100, max_chars=100, placeholder="Deixe aqui seu comentário")
    btn = st.form_submit_button("Enviar", help="Registra a avaliação no sistema", on_click=None)
    
    if btn:
        if gestor == '':
            st.error("Selecione o gestor!")
        else:
            try:
                feedback = FeedbackController().create_feedback(gestor, colaborador, voto, comments)
                st.success("Avaliação registrada com sucesso!")
                st.balloons()
            except Exception as e:
                st.error("Erro ao registrar avaliação!")
                st.error(e)
