# AI Agent Day Trade Web App

## Overview

This project is a web application designed to assist users in day trading by providing real-time analysis and insights on stock tickers. The app leverages AI agents to fetch and analyze financial data, offering visualizations and recommendations to help users make informed trading decisions.

## Features

- **Real-time Stock Analysis**: Users can input a stock ticker symbol to receive real-time analysis, including analyst recommendations and the latest news.
- **Data Visualization**: The app provides various visualizations such as stock price trends, candlestick charts, moving averages, and trading volumes.
- **User-Friendly Interface**: The app includes a sidebar with instructions and examples to guide users on how to use the application effectively.

## Technologies Used

- **Streamlit**: For building the web application interface.
- **OpenAI**: For AI-powered analysis and recommendations.
- **YFinanceTools**: For fetching financial data.
- **DuckDuckGo**: For web searches to gather the latest news and information.
- **Matplotlib/Plotly**: For creating visualizations.
- **dotenv**: For managing environment variables.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-agent-day-trade-web-app.git
   cd ai-agent-day-trade-web-app
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key to the `.env` file:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Navigate to the web interface**:
   - Open your browser and go to `http://localhost:8501`.

3. **Use the app**:
   - Enter a stock ticker symbol in the text input field.
   - Click the **Analisar** button to fetch and analyze the data.
   - View the AI-generated insights and visualizations.

## Code Structure

- **app.py**: Main file to run the Streamlit application.
- **ia_module.py**: Contains functions for interacting with AI agents.
- **analytics.py**: Contains functions for fetching and visualizing financial data.
- **.env**: Environment variables file (not included in the repository, needs to be created by the user).

## Example

### Sidebar Instructions

```markdown
### Como Utilizar a App:

- Insira o símbolo do ticker da ação desejada no campo central.
- Clique no botão **Analisar** para obter a análise em tempo real com visualizações e insights gerados por IA.

### Exemplos de tickers válidos:
- MSFT (Microsoft)
- TSLA (Tesla)
- AMZN (Amazon)
- GOOG (Alphabet)

Mais tickers podem ser encontrados aqui: https://stockanalysis.com/list/nasdaq-stocks/
```

### Main Interface


## Contact

For any inquiries or issues, please contact rafaelmagnusson98@gmail.com.

---

Feel free to reach out if you have any questions or need further assistance!