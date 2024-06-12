from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_community.llms.ollama import Ollama

llm = ChatOpenAI(model="gpt-3.5-turbo")
# llm = Ollama(model="llama2") # for Ollama users

#Step 1
text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]

# Step 3
# system_text="You are a sarcastic bot that gives helpful advice"
# messages = [SystemMessage(content=system_text), HumanMessage(content=text)]

# Step 2
llm.invoke(messages)