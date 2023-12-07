import pandas as pd
import streamlit as st
from pages import *
from controllers.colaborador_controller import ColaboradorController
from controllers.feedback_controller import FeedbackController
from streamlit_extras.metric_cards import style_metric_cards
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="Dashboard Satisfação",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

feedback_df = FeedbackController.get_all_feedbacks()
colaborador_df = ColaboradorController.get_all_colaboradores()

st.title("📊 Dashboard Satisfação")

gestor_nomes = feedback_df['gestor'].sort_values().unique()
gestor_nomes = ['Todos'] + gestor_nomes.tolist()
alocacao = feedback_df['alocacao'].sort_values().unique()

st.sidebar.title('Filtros')
find_gestor = st.sidebar.selectbox("Selecione o avaliador", gestor_nomes, placeholder="Selecione o gestor")

col1, col2, col3 = st.columns(3)

medean_feedbacks = feedback_df[feedback_df['gestor'] == find_gestor]['feedback'].mean() if find_gestor != 'Todos' else feedback_df['feedback'].mean()
total_avaliacoes = len(feedback_df[feedback_df['gestor'] == find_gestor]) if find_gestor != 'Todos' else len(feedback_df)
total_colaboradores = colaborador_df.shape[0]

col1.metric("Total de avaliações", total_avaliacoes, total_avaliacoes)
col2.metric("Média das avaliações", f'{medean_feedbacks: .2f}', f'{medean_feedbacks: .2f}')
col3.metric("Colaboradores ativos", total_colaboradores, total_colaboradores)

style_metric_cards(border_left_color="#FFFFFF", background_color="#803DF5")

new_df = pd.DataFrame(feedback_df[['gestor', 'feedback', 'alocacao']])
new_df = new_df[(new_df['gestor']==find_gestor)] if find_gestor != 'Todos' else new_df

fig = px.treemap(
    new_df,
    path=[px.Constant("Walmir Valença"), 'alocacao'],
    values='feedback',
    color='feedback',
    color_continuous_scale='purp',
    title='Treemap - Avaliação dos colaboradores',
    hover_data={'feedback': ':.2f'},
)

fig.update_traces(
    go.Treemap(
        textinfo='label+value',
        textfont=dict(size=14, family='Arial, sans-serif'),
        marker=dict(
            colorscale='purp',
            line=dict(width=2),
        ),
    )
)

fig.update_traces(marker=dict(cornerradius=5))
fig.update_traces(textfont=dict(size=14, family='Arial, sans-serif'))    

fig.update_layout(margin = dict(t=50, l=50, r=50, b=25))
st.plotly_chart(fig, use_container_width=True)
