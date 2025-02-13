# import streamlit as st
# import requests

# # FastAPI URL
# API_URL = "http://127.0.0.1:8000/chat"



# st.title("💬FAQ Bot")

# # Chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # User Input
# user_query = st.chat_input("Ask me a question...")

# if user_query:
#     st.session_state.messages.append({"role": "user", "content": user_query})
    
#     with st.chat_message("user"):
#         st.markdown(user_query)

#     # Send query to FastAPI backend
#     response = requests.post(API_URL, json={"query": user_query}).json()
#     bot_response = response.get("response", "Error: No response from server.")

#     st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
#     with st.chat_message("assistant"):
#         st.markdown(bot_response)

import os
import subprocess

# Start FastAPI server in the background
if "RUNNING_ON_SPACES" not in os.environ:
    subprocess.Popen(["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"])

import streamlit as st
import requests

# FastAPI URL (Hugging Face uses public URLs)
API_URL = "http://localhost:8000/chat"

st.title("💬FAQ Bot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_query = st.chat_input("Ask me a question...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    with st.chat_message("user"):
        st.markdown(user_query)

    # Send query to FastAPI backend
    response = requests.post(API_URL, json={"query": user_query}).json()
    bot_response = response.get("response", "Error: No response from server.")

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    with st.chat_message("assistant"):
        st.markdown(bot_response)
