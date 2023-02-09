import streamlit as st

import pandas as pd
import pandas_datareader.data as web
import numpy as nump

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from datetime import datetime

import yfinance as yf
yf.pdr_override()


st.sidebar.title('Menu')


# Lista das emoresasa - tciker b3
Empresas =['KLBN11.SA','WEGE3.SA']
Selecao = st.sidebar.selectbox('Selecione a empresa: ', Empresas)

# Range de seleção
Range = st.sidebar.slider('Período de meses', 0, 12, 1, key='Barra_Seleção')
Selecao_Range = str(Range)+'mo'

# Colunas 
col1,col2 = st.columns([0.9, 0.1])

# Imagens
Imagens = [
'https://www.weg.net/institutional/_ui/desktop/theme-institutional/img/img-standard-share.jpg',
'https://www.suno.com.br/wp-content/uploads/2018/03/faturamento-klabin.jpg'
]
# Título
Titulo = f'Análise Econômica { str(Selecao)}'
col1.title(Titulo)

if Selecao == 'WEGE3.SA':
    col2.image( Imagens[0], width=70 )
else:
    col2.image( Imagens[1], width=70 )

# Coletar da API do Yahoo
Dados = web.get_data_yahoo( Selecao, period=Selecao_Range)

Grafico_Candlestiick = go.Figure(
    data=[
        go.Candlestick(
            x=Dados.index,
            open=Dados[ 'Open'],
            high=Dados[ 'High'],
            low=Dados[ 'Low'],
            close=Dados['Close']

        )
    ]
)

Grafico_Candlestiick.update_layout(
    xaxis_rangeslider_visible=False,
    title=' Análise das ações',
    xaxis_title='Período',
    yaxis_title='Preço'

)

# Mostrar o gráfico do plotly no streamlit
st.plotly_chart( Grafico_Candlestiick)
# condição
if st.checkbox('Mostrar dados em tabela'):
    st.subheader('Tabela de registros')
    st.write( Dados )