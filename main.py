## Integrate our code Open AI
import openai
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

# runs multiple promts but shows only result of last prompt
from langchain.chains import SimpleSequentialChain

# runs multiple promts and shows only result one after another
from langchain.chains import SequentialChain

from langchain.memory import ConversationBufferMemory

import streamlit as st


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


# steamlit framework

st.title("Langchain Demo with OpenAI API")
input_text = st.text_input("Type the topic you want to search")

# Prompt Template 1
first_input_prompt = PromptTemplate(
    input_variables=["name"], template="Tellme about celebrity {name}"
)

# Memory

person_memory = ConversationBufferMemory(input_key="name", memory_key="chat_history")
dob_memory = ConversationBufferMemory(input_key="person", memory_key="chat_history")
description_memory = ConversationBufferMemory(
    input_key="dob", memory_key="description_history"
)

# OpenAI LLMS
llm = OpenAI(temperature=0.8)
chain1 = LLMChain(
    llm=llm,
    prompt=first_input_prompt,
    verbose=True,
    output_key="person",
    memory=person_memory,
)


# Prompt Template 2
second_input_prompt = PromptTemplate(
    input_variables=["person"], template="when {person} was born"
)

chain2 = LLMChain(
    llm=llm,
    prompt=second_input_prompt,
    verbose=True,
    output_key="dob",
    memory=dob_memory,
)


# Prompt Template 3
third_input_prompt = PromptTemplate(
    input_variables=["dob"],
    template="mention 5 major events happend around {dob} in India",
)

chain3 = LLMChain(
    llm=llm,
    prompt=third_input_prompt,
    verbose=True,
    output_key="Description",
    memory=description_memory,
)


parent_chain = SequentialChain(
    chains=[chain1, chain2, chain3],
    input_variables=["name"],
    output_variables=["person", "dob", "Description"],
    verbose=True,
)

if input_text:
    st.write(parent_chain({"name": input_text}))

    with st.expander("Person Name"):
        st.info(person_memory.buffer)

    with st.expander("Major Events"):
        st.info(description_memory.buffer)
