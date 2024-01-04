import streamlit as st
import random
import time

# st.set_page_config(layout="wide")

st.title("Red Hat Docs Chatbot")

responses = [
    "Hello there! How can I assist you today?",
    "Red Hat OpenShift AI is an open-source, container-based platform that provides machine learning and deep learning capabilities to developers and IT operations teams. It enables the creation, deployment, and management of AI applications on Kubernetes clusters, making it easy to build, train, and run AI models at scale. With OpenShift AI, organizations can accelerate their AI initiatives and innovate faster by leveraging the power of Kubernetes and the open-source AI community.",
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
