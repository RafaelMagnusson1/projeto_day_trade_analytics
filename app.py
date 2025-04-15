import re
import streamlit as st
from dotenv import load_dotenv
import ia_module as ia
import analytics as anl

st.title("AI Agent day trade Web App")

#Configurações da sidebar

st.sidebar.title("Instruções")
st.sidebar.markdown("""
### Como Utilizar a App:

- Insira o símbolo do ticker da ação desejada no campo central.
- Clique no botão **Analisar** para obter a análise em tempo real com visualizações e insights gerados por IA.

### Exemplos de tickers válidos:
- MSFT (Microsoft)
- TSLA (Tesla)
- AMZN (Amazon)
- GOOG (Alphabet)

Mais tickers podem ser encontrados aqui: https://stockanalysis.com/list/nasdaq-stocks/

""")

#Configuração do app

ticker = st.text_input("Digite o Código (símbolo do ticker):").upper()


if st.button("Analisar"):

    with st.spinner("Buscando os Dados em Tempo Real. Aguarde..."):      
        hist = anl.extract_ticker_data(ticker=ticker)

        ai_response = ia.multi_ai_agent.run(f"Resumir a recomendação do analista e compartilhar as últimas notícias para {ticker}")

        clean_response = re.sub(r"(Running:[\s\S]*?\n\n)|(^transfer_task_to_finance_ai_agent.*\n?)","", ai_response.content, flags=re.MULTILINE).strip()
        st.markdown(clean_response)

        st.subheader("Visualização dos Dados")

        anl.plot_stock_price(hist, ticker)
        anl.plot_candlestick(hist, ticker)
        anl.plot_media_movel(hist, ticker)
        anl.plot_volume(hist, ticker)