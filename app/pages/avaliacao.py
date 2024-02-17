import streamlit as st
from controllers.avaliacoes_controller import AvaliacaoController as ac
from controllers.colaborador_controller import ColaboradorController as cc
from controllers.desemepnho_controller import DesempenhoController as dc
from controllers.produtividade_controller import ProdutividadeController as pc

# Configurações da página
st.set_page_config(
    page_title="Dashboard Satisfação",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.cache_resource.clear()

@st.cache_resource
def get_gestores():
    gestores = cc.get_all_gestores()
    gestores_lista = [(gestor[0], gestor[1]) for gestor in gestores]
    return gestores_lista

@st.cache_resource
def get_setores():
    setores = cc.get_all_setores()
    setores_lista = [(setor[0], setor[1]) for setor in setores]
    return setores_lista

@st.cache_resource
def get_colaboradores(page, page_size):
    colaboradores = cc.get_all_colaboradores(page, page_size)
    return colaboradores

def main():

    st.cache_resource.clear()

    gestores = get_gestores()
    setores = get_setores()
    colaboradores = get_colaboradores(1, 100)

    gestores_lista = ['', *[nome for id, nome in gestores]]
    setores_lista = ['', *[nome for id, nome in setores]]


    st.title("📋 Registre aqui sua avaliação")

    with st.form(key='form-avaliacao', clear_on_submit=True):
        gestor = st.selectbox("Gestor", gestores_lista, key="gestor", index=0, help="Selecione o gestor")
        gestor_id = [id for id, nome in gestores if nome == gestor][0] if gestor != '' else ''
        
        
        setor = st.selectbox("Setor", setores_lista, index=0, key="setor", help="Selecione o setor")
        setor_id = [id for id, nome in setores if nome == setor][0] if setor != '' else ''
        
        colaborador = st.selectbox("Colaborador", ['', *[item.nome for item in colaboradores.itertuples()]], index=0, key="colaborador", help="Selecione o colaborador")
        colaborador_id = [item.id for item in colaboradores.itertuples() if item.nome == colaborador][0] if colaborador != '' else ''

        st.subheader("| Avalie o desempenho do colaborador")
        col1, col2 = st.columns(2)
        opcoes = ['🙁 Desconectado', '😐 Insatisfeito', '🙂 Conectado', '🤩 Excepicional', '🚫 Impossível opinar']
        voto_desempenho = col1.radio("Como você avalia o desempenho do colaborador?", opcoes, index=0, key="feedback", help="Selecione uma opção")
        voto_desempenho = 1 if voto_desempenho == "🙁 Desconectado" else 2 if voto_desempenho == "😐 Insatisfeito" else 3 if voto_desempenho == "🙂 Conectado" else 4 if voto_desempenho == '🤩 Excepicional' else 5
        comments = col2.text_area("Comentário", key="comment", height=100, max_chars=100, placeholder="Deixe aqui seu comentário", disabled=True if voto_desempenho == 5 else False, help="Deixe um comentário sobre o desempenho do colaborador")

        st.write("---")
        st.subheader("| Avalie a produtividade do colaborador")

        col1, col2 = st.columns(2)

        voto_produtividade = col1.slider("Qualidade do trabalho (De 0 a 5)", 0, 5, 0, key="feedback_produtividade", help="Avalie a qualidade do trabalho do colaborador")
        bateu_meta = st.radio("Colaborador bateu a meta?", ["Sim", "Não", "Não tem meta"], index=0, key="bateu_meta", help="Selecione uma opção")
        comments_produtividade = col2.text_area("*Justifique sua nota!", key="comment_produtividade", height=100, max_chars=100, placeholder="Deixe aqui seu comentário", help="Deixe um comentário sobre a qualidade do trabalho do colaborador")
        st.write("---")
        btn = st.form_submit_button("Enviar", on_click=None)


        if btn:
            if gestor == '' or setor == '' or colaborador == '' or voto_desempenho == 0 or (voto_produtividade <= 3 and comments_produtividade == ''):
                st.error("Preencha todos os campos!")
            else:
                id_engajamento = dc().create_desempenho(colaborador_id, gestor_id, voto_desempenho, comments)
                id_produtividade = pc().create_produtividade(colaborador_id, gestor_id, voto_produtividade, comments_produtividade, bateu_meta)
                ac().create_avaliacao(colaborador_id, id_engajamento, id_produtividade)

                st.success("Avaliação registrada com sucesso!")
                st.cache_resource.clear()                

if __name__ == "__main__":
    main()

# Path: app/pages/Avaliacao.py
    