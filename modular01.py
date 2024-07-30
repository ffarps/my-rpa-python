import streamlit as st
import random
import string


class ChatbotState:
    # INITIAL = "initial"
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
    st.session_state.chat_state = ChatbotState.CONFIRM_NAME
    st.session_state.response = "Let's start the check-in process. What is your name?"


def confirm_name(name):
    st.session_state.user_name = name
    st.session_state.response = f"Is your name {name}? (yes/no)"
    st.session_state.chat_state = ChatbotState.ASK_EMAIL


def ask_email():
    st.session_state.response = "Please provide your email address."
    st.session_state.chat_state = ChatbotState.CONFIRM_EMAIL


def confirm_email(email):
    st.session_state.user_email = email
    st.session_state.response = f"Is your email {email}? (yes/no)"
    st.session_state.chat_state = ChatbotState.CHECK_IN


def generate_reservation_number(length=6):
    characters = string.ascii_uppercase + string.digits
    return "".join(random.choices(characters, k=length))


def check_in():
    reservation_number = generate_reservation_number()
    st.session_state.chat_state = ChatbotState.DONE
    st.session_state.response = f"Check-in complete for {st.session_state.user_name} with email {st.session_state.user_email}. Your reservation code is {reservation_number}."


def reset_chat():
    st.session_state.chat_state = ChatbotState.ASK_NAME
    st.session_state.messages = []
    st.session_state.user_name = ""
    st.session_state.user_email = ""
    st.session_state.response = "Let's start the check-in process. What is your name?"


def handle_input(user_input):
    state = st.session_state.chat_state
    if state == ChatbotState.ASK_NAME:
        st.session_state.chat_state = ChatbotState.CONFIRM_NAME
        ask_name()
        ##print(f"Asking name: {user_input}")
    elif state == ChatbotState.CONFIRM_NAME:
        confirm_name(user_input)
        # print(f"Confirming name: {user_input}")
    elif state == ChatbotState.ASK_EMAIL:
        ask_email()
        # print(f"Asking email: {user_input}")
    elif state == ChatbotState.CONFIRM_EMAIL:
        confirm_email(user_input)
        # print(f"Confirming email: {user_input}")
    elif state == ChatbotState.CHECK_IN:
        check_in()
        # print(f"check in: {user_input}")

    # if state == ChatbotState.INITIAL:
    #     ask_name()
    # elif state == ChatbotState.ASK_NAME:
    #     confirm_name(user_input)
    # elif state == ChatbotState.CONFIRM_NAME:
    #     if user_input.lower() == "yes":
    #         ask_email()
    #     else:
    #         ask_name()
    # elif state == ChatbotState.ASK_EMAIL:
    #     confirm_email(user_input)
    # elif state == ChatbotState.CONFIRM_EMAIL:
    #     if user_input.lower() == "yes":
    #         check_in()
    #     else:
    #         ask_email()


def simplebot():
    st.title("Check-in Bot")
    st.caption("State: " + st.session_state.chat_state)

    if "messages" not in st.session_state:
        st.session_state.messages = []
        reset_chat()
    if st.session_state.chat_state != ChatbotState.DONE:
        user_input = st.chat_input("your response")
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
