import streamlit as st
import gc
import random
import string
from define_type_of_flow import define_type_of_flow

greetings = ["hello", "hi", "hey", "greetings", "what's up"]
responses = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
checkins = ["check", "in", "checkin"]
checkin_responses = [
    "For checking in, please give me your name and your email address. Thank you!",
    "I will check in with you, please give me your name and your email address. Thank you!",
]

# Initialize session state variables
if "type_of_flow" not in st.session_state:
    st.session_state.type_of_flow = "None"
if "custom_flow" not in st.session_state:
    st.session_state.custom_flow = False


def reset_chat():
    st.session_state.messages = []
    st.session_state.context = None
    st.session_state.custom_flow = False  # Reset custom flow state
    st.session_state.type_of_flow = "None"  # Reset type of flow
    gc.collect()


def preprocess_text_before_sending_to_gpt(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()
    return tokens


def generate_response_from(user_input):
    tokens = preprocess_text_before_sending_to_gpt(user_input)
    if any(token in greetings for token in tokens):
        return random.choice(responses)
    elif "check" in tokens and ("in" in tokens or "checkin" in tokens):
        st.session_state.custom_flow = True
        st.session_state.type_of_flow = "checkin"
        st.session_state.messages.append(
            {"role": "assistant", "content": random.choice(checkin_responses)}
        )
        st.rerun()

    return "I'm here to help, but I don't have the answer to that."


def simplebot():
    st.title("Simple Check in Virtual Assistant Bot")
    st.caption(
        f"Type of flow: {st.session_state.type_of_flow} | Custom flow: {st.session_state.custom_flow}"
    )
    if "messages" not in st.session_state:
        st.session_state.messages = []
        reset_chat()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if not st.session_state.custom_flow:
        if prompt := st.chat_input("Ask me anything"):
            st.chat_message("user").markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            try:
                response = generate_response_from(prompt)
            except Exception as e:
                response = str(e)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    else:
        define_type_of_flow(st.session_state.type_of_flow)
    st.button("Clear Chat", on_click=reset_chat)


simplebot()
