import streamlit as st
import gc


def reset_chat():
    st.session_state.messages = []
    st.session_state.context = None
    gc.collect()


def generate_response(user_input):
    if "hello" or "hi" in user_input.lower():
        return "Hi there!, how can I assist you?"
    elif "who are you" in user_input.lower():
        return "I'm the simple Bot. Ask me anything."
    elif "check in" in user_input.lower():
        return "Sure, I'll check you in, but first I need your name"
    else:
        return "I'm here to help, but I don't have the answer to that."


def simplebot():
    # st.title("Simple Bot")
    # st.caption("Ask me anything!")

    if "messages" not in st.session_state:
        st.session_state.messages = []
        reset_chat()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me anything"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        # for now, response comes from a function that returns a couple of strings
        try:
            response = generate_response(prompt)
        except Exception as e:
            response = str(e)

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.button("Clear Chat", on_click=reset_chat)


simplebot()
