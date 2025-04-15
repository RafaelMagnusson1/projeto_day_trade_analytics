#Módulo de analytics

#Módulo com a finalidade de conter os dados de analytics do ticker inputado na UI


import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def extract_ticker_data(ticker, period="6mo"):

    stock = yf.Ticker(ticker)
    
    hist = stock.history(period=period)
    
    hist.reset_index(inplace=True)

    return hist


def plot_stock_price(hist, ticker):

    fig = px.line(hist, x="Date", y="Close", title=f"{ticker} Preços das Ações (Últimos 6 Meses)", markers=True)
    
    st.plotly_chart(fig)


def plot_candlestick(hist, ticker):

    fig = go.Figure(

        data=[go.Candlestick(x=hist['Date'],        # Define as datas no eixo X
                             open=hist['Open'],     # Define os preços de abertura
                             high=hist['High'],     # Define os preços mais altos
                             low=hist['Low'],       # Define os preços mais baixos
                             close=hist['Close'])]  # Define os preços de fechamento
    )
    
    fig.update_layout(title=f"{ticker} Candlestick Chart (Últimos 6 Meses)")
    
    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig)


def plot_media_movel(hist, ticker):

    hist['SMA_20'] = hist['Close'].rolling(window=20).mean()
    
    hist['EMA_20'] = hist['Close'].ewm(span=20, adjust=False).mean()
    
    fig = px.line(hist, 
                  x='Date', 
                  y=['Close', 'SMA_20', 'EMA_20'],
                  title=f"{ticker} Médias Móveis (Últimos 6 Meses)",  
                  labels={'value': 'Price (USD)', 'Date': 'Date'})    

    st.plotly_chart(fig)


def plot_volume(hist, ticker):


    fig = px.bar(hist, 
                 x='Date', 
                 y='Volume', 
                 title=f"{ticker} Trading Volume (Últimos 6 Meses)")  # Define o título do gráfico
    

    st.plotly_chart(fig)
