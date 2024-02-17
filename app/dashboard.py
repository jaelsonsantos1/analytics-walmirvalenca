import streamlit as st
from pages import *
from controllers.avaliacoes_controller import AvaliacaoController as ac
from streamlit_extras.metric_cards import style_metric_cards
import plotly.express as px
import plotly.graph_objects as go
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(
    page_title="Dashboard Satisfação",
    page_icon="📊",
    layout="wide",
)

# @st.cache_resource()
def get_avaliacoes():
    avaliacoes = ac().avaliacoes()
    df = avaliacoes[['Colaborador', 'Engajamento', 'Produtividade', 'Setor', 'Gestor']]
    return df

avaliacoes = get_avaliacoes()

st.title("📊 Dashboard Satisfação")

def card():
    # Adicionar cards com a média de engajamento e produtividade e total de colaboradores
    media_engajamento = avaliacoes['Engajamento'].mean()
    media_produtividade = avaliacoes['Produtividade'].mean()
    total_colaboradores = avaliacoes['Colaborador'].nunique()

    col1, col2, col3 = st.columns(3)

    col1.metric(label="Média de Desempenho", value=f'{media_engajamento: .2f}', delta=0)
    col2.metric(label="Média de Produtividade", value=f'{media_produtividade: .2f}', delta=0)
    col3.metric(label="Colaboradores Ativos", value=total_colaboradores, delta=0)

    style_metric_cards(
        # background dark
        background_color="#00000",
        box_shadow="0 10px 10px 0 rgba(255, 255, 255, 0.5)",
        border_radius_px=10,
        border_size_px=None,
        border_left_color="#FFFF",
    )

card()


st.write('---')

avaliacoes['wva'] = "Walmir Valença Advogados"

# Tree Map - Média de Engajamento de colaboradores dividido por setor
media_engajamento = avaliacoes.groupby(['wva', 'Setor', 'Colaborador'])['Engajamento'].mean().reset_index().round(2)

columns = st.columns(2)
fig = px.treemap(media_engajamento, path=['wva', 'Setor', 'Colaborador'], values='Engajamento', title='| Média de Engajamento por Colaborador', color='Engajamento', color_continuous_scale='Teal')
fig.update_traces(textinfo='label+value+percent entry')
# Formatar os textos
fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
fig.update_layout(font_family='Arial', font_size=14, font_color='white')
columns[0].plotly_chart(fig)


# Pie Chart - Média de Engajamento de colaboradores dividido por setor
media_engajamento = avaliacoes.groupby(['wva', 'Setor'])['Engajamento'].mean().reset_index().round(2)
fig = px.pie(media_engajamento, values='Engajamento', names='Setor', title='| Média de Engajamento por Setor', color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
fig.update_layout(font_family='Arial', font_size=14, font_color='white')
st.plotly_chart(fig)

# Agrupar avaliação de engajamento dos colaboradores por gestor
avaliacoes_gestor = avaliacoes.groupby(['Gestor', 'Colaborador'])['Engajamento'].mean().reset_index().round(2)

# Adicionar em um gráfico de barras - eixo x: colaborador, eixo y: média de engajamento, cor: gestor
fig = px.bar(avaliacoes_gestor, x='Colaborador', y='Engajamento', color='Gestor', title='| Média de Engajamento por Colaborador', text='Engajamento', color_discrete_sequence=px.colors.qualitative.Pastel, range_y=[0, 5])
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
fig.update_layout(font_family='Arial', font_size=14, font_color='white')
columns[1].plotly_chart(fig)


st.write('---')

# Tree Map - Média de produtividade de colaboradores dividido por setor
columns = st.columns(2)
media_produtividade = avaliacoes.groupby(['wva', 'Setor', 'Colaborador'])['Produtividade'].mean().reset_index().round(2)
fig = px.treemap(media_produtividade, path=['wva', 'Setor', 'Colaborador'], values='Produtividade', title='| Média de Produtividade por Colaborador', color='Produtividade', color_continuous_scale='OrRd')
fig.update_traces(textinfo='label+value+percent entry')

# Formatar os textos
fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
fig.update_layout(font_family='Arial', font_size=14, font_color='white')
columns[0].plotly_chart(fig)

# Agrupar avaliação de produtividade dos colaboradores por gestor
avaliacoes_gestor = avaliacoes.groupby(['Gestor', 'Colaborador'])['Produtividade'].mean().reset_index().round(2)

# Adicionar em um gráfico de barras - eixo x: colaborador, eixo y: média de produtividade, cor: gestor
fig = px.bar(avaliacoes_gestor, x='Colaborador', y='Produtividade', color='Gestor', title='| Média de Produtividade por Colaborador', text='Produtividade', color_discrete_sequence=px.colors.qualitative.Pastel,)
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
fig.update_layout(font_family='Arial', font_size=14, font_color='white')
columns[1].plotly_chart(fig)

# Pie Chart - Média de Engajamento de colaboradores dividido por setor
media_produtividade = avaliacoes.groupby(['wva', 'Setor'])['Produtividade'].mean().reset_index().round(2)
fig = px.pie(media_produtividade, values='Produtividade', names='Setor', title='| Média de Produtividade por Setor', color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
fig.update_layout(font_family='Arial', font_size=14, font_color='white')
st.plotly_chart(fig)

st.write('---')



