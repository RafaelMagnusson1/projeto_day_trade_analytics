from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
from dotenv import load_dotenv
from openai import OpenAI
import os
from phi.agent import Agent, RunResponse
from phi.model.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    markdown=True
)

# Carregar variáveis do arquivo .env
load_dotenv()

# Configurar a chave da API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Agente de busca na Web:

agente_web_search = Agent(
    name="Agente Web Search",
    model=OpenAIChat(id="gpt-4o"),
    role="Fazer busca na web",
    tools=[DuckDuckGo()],
    instructions=["Sempre inclua as fontes"],
    show_tool_calls=True,
    markdown=True
)

# Agente financeiro
agente_financeiro = Agent(
    name="Agente Financeiro",
    model=OpenAIChat(id="gpt-4o"),
    role="Fornecer informações financeiras",
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         stock_fundamentals=True,
                         company_news=True)],
    instructions=["Use tabelas para mostrar os dados"],
    show_tool_calls=True,
    markdown=True
)

# Definindo o agente multi AI
multi_ai_agent = Agent(
    team=[agente_web_search, agente_financeiro],
                       model=OpenAIChat(id="gpt-4o"),
                       instructions=["Sempre inclua as fontes", "Use tabelas para mostrar os dados"],
                       show_tool_calls=True, markdown=True)


