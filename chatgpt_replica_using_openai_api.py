
#!pip install -qU langchain langchain-openai langchain-google-genai
import os
from getpass import getpass
os.environ['OPENAI_API_KEY'] = " #add api key here"

# Using OpenAI Models (GPT 3.5)
#!pip install langchain_openai
from langchain_openai import ChatOpenAI
gpt3_model = ChatOpenAI(model = "gpt-3.5-turbo-0125" , temperature=0.3)

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory

memory = ConversationBufferMemory(k=5)
conversation = ConversationChain(
    llm= gpt3_model,
    memory=memory
)

conversation.predict(input="#ask your question")