import streamlit as st
import random
import time

# st.set_page_config(layout="wide")

st.title("Chatbot")

responses = [
    # "Hello there! How can I assist you today?",
    "There is no specific technology or platform known as OpenShift AI. OpenShift is a container orchestration platform developed by Red Hat. It enables organizations to deploy, manage, and scale containerized applications. Containers provide a lightweight and consistent environment for applications to run, making it easier to move applications between different environments.",
    "You're Welcome!"
]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Questions?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        if 'response_index' not in st.session_state:
            st.session_state.response_index = 0
        assistant_response = responses[st.session_state.response_index]
        st.session_state.response_index = (st.session_state.response_index + 1) % len(responses)
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
