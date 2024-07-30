import streamlit as st
import random
import string


class ChatbotState:
    ASK_NAME = "ask_name"
    CONFIRM_NAME = "confirm_name"
    ASK_EMAIL = "ask_email"
    CONFIRM_EMAIL = "confirm_email"
    CHECK_IN = "check_in"
    DONE = "done"


if "chat_state" not in st.session_state:
    st.session_state.chat_state = ChatbotState.ASK_NAME
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "response" not in st.session_state:
    st.session_state.response = (
        "Welcome! Let's start the check-in process. What is your name?"
    )


def ask_name():
    st.session_state.response = "What is your name?"


def confirm_name(name):
    st.session_state.user_name = name
    st.session_state.response = f"Is your name {name}? (yes/no)"


def ask_email():
    st.session_state.response = "Please provide your email address."


def confirm_email(email):
    st.session_state.user_email = email
    st.session_state.response = f"Is your email {email}? (yes/no)"


def generate_reservation_number(length=6):
    characters = string.ascii_uppercase + string.digits
    return "".join(random.choices(characters, k=length))


def check_in():
    reservation_number = generate_reservation_number()
    st.session_state.response = f"Check-in complete for {st.session_state.user_name} with email {st.session_state.user_email}. Your reservation code is {reservation_number}."
    st.session_state.chat_state = ChatbotState.DONE


def reset_chat():
    st.session_state.chat_state = ChatbotState.ASK_NAME
    st.session_state.user_name = ""
    st.session_state.user_email = ""
    st.session_state.response = (
        "Welcome! Let's start the check-in process. What is your name?"
    )
    st.session_state.messages = [
        {"role": "Assistant", "content": st.session_state.response}
    ]


def handle_input(user_input):
    state = st.session_state.chat_state

    if state == ChatbotState.ASK_NAME:
        confirm_name(user_input)
        st.session_state.chat_state = ChatbotState.CONFIRM_NAME
    elif state == ChatbotState.CONFIRM_NAME:
        if user_input.lower() == "yes":
            ask_email()
            st.session_state.chat_state = ChatbotState.ASK_EMAIL
        else:
            ask_name()
            st.session_state.chat_state = ChatbotState.ASK_NAME
    elif state == ChatbotState.ASK_EMAIL:
        confirm_email(user_input)
        st.session_state.chat_state = ChatbotState.CONFIRM_EMAIL
    elif state == ChatbotState.CONFIRM_EMAIL:
        if user_input.lower() == "yes":
            check_in()
        else:
            ask_email()
            st.session_state.chat_state = ChatbotState.ASK_EMAIL


def simplebot():
    # st.title("Check-in Bot")
    st.caption("`State: " + st.session_state.chat_state + "`")

    if "messages" not in st.session_state:
        reset_chat()

    if st.session_state.chat_state != ChatbotState.DONE:
        user_input = st.chat_input("Your response")
        if user_input:
            handle_input(user_input)
            st.session_state.messages.append({"role": "User", "content": user_input})
            st.session_state.messages.append(
                {"role": "Assistant", "content": st.session_state.response}
            )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    st.button("Restart", on_click=reset_chat)


simplebot()
