import streamlit as st
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

gestores = cc.get_all_gestores()
setores = cc.get_all_setores()
colaboradores = cc.get_all_colaboradores()[['id', 'nome', 'idade', 'id_gestor', 'gestor', 'id_setor', 'setor', 'created_at']]

gestores_lista = ['', *[nome for id, nome in gestores]]
setores_lista = ['', *[nome for id, nome in setores]]

btn_voto_nulo = None


st.title("Registre aqui sua avaliação")

st.write("---")

col1, col2, col3 = st.columns(3)
gestor = col1.selectbox("Gestor", gestores_lista, key="gestor", index=0, help="Selecione o gestor")
gestor_id = [id for id, nome in gestores if nome == gestor][0] if gestor != '' else ''
setor = col2.selectbox("Setor", setores_lista, index=0, key="setor", help="Selecione o setor")
setor_id = [id for id, nome in setores if nome == setor][0] if setor != '' else ''
colaboradores_setor = [col.nome for col in colaboradores.itertuples() if col.id_setor == setor_id]
colaborador = col3.selectbox("Colaborador", ['', *[nome for nome in colaboradores_setor]], index=0, key="colaborador", help="Selecione o colaborador")
colaborador_id = [col.id for col in colaboradores.itertuples() if col.nome == colaborador][0] if colaborador != '' else ''
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
if voto_produtividade <= 3:
    comments_produtividade = col2.text_area("*Justifique sua nota!", key="comment_produtividade", height=100, max_chars=100, placeholder="Deixe aqui seu comentário", help="Deixe um comentário sobre a qualidade do trabalho do colaborador")
else:
    comments_produtividade = col2.text_area("Comentário", key="comment_produtividade", height=100, max_chars=100, placeholder="Deixe aqui seu comentário", disabled=True, help="Deixe um comentário sobre a qualidade do trabalho do colaborador")
st.write("---")
#  Botão enviar na cor verde
btn = st.button("Enviar", on_click=None)    

if btn:
    if gestor == '' or setor == '' or colaborador == '' or voto_desempenho == 0 or (voto_produtividade <= 3 and comments_produtividade == ''):
        st.error("Preencha todos os campos!")
    else:
        dc().create_desempenho(colaborador_id, gestor_id, voto_desempenho, comments)
        st.success("Avaliação de desempenho registrada com sucesso!")
        pc().create_produtividade(colaborador_id, gestor_id, voto_produtividade, comments_produtividade, bateu_meta)
        st.success("Avaliação de produtividade registrada com sucesso!")

        st.balloons()