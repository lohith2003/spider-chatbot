import openai  
import streamlit as st

st.title("Spider")

openai.api_key = "sk-4MJoWKXDfMU-q5jq9SwgcZbXD_dhkqEEozzhcYL5bfT3BlbkFJ9eGA8tbzC0CgWKHJ0dAY-nzKwTvliouqI4kP6978gA"  # Replace with your actual API key

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state or not isinstance(st.session_state.messages, list):
    st.session_state.messages = []

# Displaying the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to input
prompt = st.chat_input("What is up?")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Use the updated API method
            response = openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            )
            full_response = response['choices'][0]['message']['content']
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
