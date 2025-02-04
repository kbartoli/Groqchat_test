import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1) Set up prompt template
prompt = ChatPromptTemplate(
    [
        ("system", "You are an experienced project manager with PMP certification. Please resond to queries."),
        ("user","Question:{question}")
    ]
)

# 2) Set function to generate response
def generate_response(question, engine, api_key):
    llm=ChatGroq(model=engine, api_key=api_key)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({"question":question})
    return answer

# 3) create web app with sidebar and main interface
st.title("Chatbot using Groq")

st.sidebar.title("Settings")

api_key = st.sidebar.text_input("Groq API Key", type = "password")

engine = st.sidebar.selectbox("Select LLM model", ["gemma2-9b-it", "llama-3.2-8b-instant"])

st.write("Ask your question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(question=user_input, engine=engine, api_key=api_key)
    st.write(response)
else:
    st.write("Please provide input")
