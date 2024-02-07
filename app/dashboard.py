import pandas as pd
import streamlit as st
from pages import *
from controllers.colaborador_controller import ColaboradorController as cc
from streamlit_extras.metric_cards import style_metric_cards
import plotly.express as px
import plotly.graph_objects as go
import squarify

st.set_page_config(
    page_title="Dashboard Satisfação",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def load_avaliacoes():
    return cc.get_all_avaliacoes ()

st.title("📊 Dashboard Satisfação")

# Criar 3 cards para exibir a média das notas de produtividade e engajamento e a quantidade de colaboradores
avaliacoes = load_avaliacoes()

st.dataframe(avaliacoes)

