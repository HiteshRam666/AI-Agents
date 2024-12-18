from phi.agent import Agent 
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq 
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv, find_dotenv

load_dotenv()

web_agent = Agent(
    name = "Web Agent", 
    model = OpenAIChat(id = "gpt-4o"),
    tools = [DuckDuckGo()], 
    instructions=["Always include sources"], 
    show_tool_calls=True, 
    markdown=True
)

finance_agent = Agent(
    name = "Finance Agent", 
    role = "Get financial Data",
    model = OpenAIChat(id = "gpt-4o"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    show_tool_calls=True, 
    markdown=True,
)

agent_team = Agent(
    model = OpenAIChat(id = "gpt-4o"),
    team = [web_agent, finance_agent], 
    instructions=["Always include sources", "Use tables to display data"], 
    show_tool_calls=True, 
    markdown=True,
)

agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)