from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Configurar a chave da API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIAgent(Agent):
    def __init__(self, name, role, tools, instructions, show_tool_calls, markdown):
        super().__init__(name=name, role=role, tools=tools, instructions=instructions, show_tool_calls=show_tool_calls, markdown=markdown)

    def call_openai(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        return response.choices[0].message['content']

# Definindo o agente de busca na web
agente_web_search = OpenAIAgent(
    name="DSA Agente Web Search",
    role="Fazer busca na web",
    tools=[DuckDuckGo()],
    instructions=["Sempre inclua as fontes"],
    show_tool_calls=True,
    markdown=True
)

# Definindo o agente financeiro
agente_financeiro = OpenAIAgent(
    name="DSA Agente Financeiro",
    role="Fornecer informações financeiras",
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         stock_fundamentals=True,
                         company_news=True)],
    instructions=["Use tabelas para mostrar os dados"],
    show_tool_calls=True,
    markdown=True
)

class MultiAIAgent(OpenAIAgent):
    def __init__(self, name, role, agents, instructions, show_tool_calls, markdown):
        super().__init__(name=name, role=role, tools=[], instructions=instructions, show_tool_calls=show_tool_calls, markdown=markdown)
        self.agents = agents

    def call_agent(self, agent_name, prompt):
        agent = self.agents.get(agent_name)
        if agent:
            return agent.call_openai(prompt)
        else:
            return f"Agente {agent_name} não encontrado."

# Definindo o agente multi AI
multi_ai_agent = MultiAIAgent(
    name="Multi AI Agent",
    role="Coordenação de múltiplos agentes",
    agents={
        "web_search": agente_web_search,
        "financeiro": agente_financeiro
    },
    instructions=["Sempre inclua as fontes", "Use tabelas para mostrar os dados"],
    show_tool_calls=True,
    markdown=True
)

ticker = 'MSFT'
prompt_financeiro = f"Resumir a recomendação do analista e compartilhar as últimas notícias para {ticker}"
prompt_web_search = f"Buscar as últimas notícias sobre {ticker}"

# Chamando ambos os agentes
resultado_financeiro = multi_ai_agent.call_agent("financeiro", prompt_financeiro)
resultado_web_search = multi_ai_agent.call_agent("web_search", prompt_web_search)

# Combinando os resultados
i_response = f"**Recomendações de Analistas e Notícias Financeiras para {ticker}:**\n\n{resultado_financeiro}\n\n**Últimas Notícias da Web sobre {ticker}:**\n\n{resultado_web_search}"

print(i_response)
