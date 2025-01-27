import os 
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st


load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Create out chat prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant Kindly respond to the question asked."),
        ("user", "Question: {question}"),
    ]
)

# Stramlit interface
st.title("Chat with Ollama:gamma2:2b")
input_text = st.text_input("Enter your question here: ")

llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text})
)