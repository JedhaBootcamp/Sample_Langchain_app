#!/usr/bin/env python
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_mistralai import ChatMistralAI
from langserve import add_routes

# 1. Create prompt template
# Here we create a simple prompt with two inputs 
# First a "system" prompt that corresponds to the instruction for the model 
# Second a "user" prompt that corresponds to what a user inputs when interacting with the model
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
# Here we chose a model from Mistral
# Generally you should always try to use Chat models even if the purpose of the app is not to chat
model = ChatMistralAI(model="mistral-large-latest")

# 3. Create parser
# This simply outputs the result of the LLM as pure string
parser = StrOutputParser()

# 4. Create chain
# Here we create a workflow that 
# First -> Read the prompt 
# Second -> Apply the model on the given prompt 
# Third -> Output the result as a string 
chain = prompt_template | model | parser

# 5. App definition
# Here we instanciate a FastAPI application
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 6. Adding chain route
# Finally this is a LangServe Wrapper that creates a endpoint at /chain 
# with a playground that you can play with at /chain/playground when the server is up
add_routes(
    app,
    chain,
    path="/chain",
)