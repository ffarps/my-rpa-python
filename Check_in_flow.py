import streamlit as st


def check_in_flow():

    if prompt := st.chat_input("Your Full name "):
        if prompt != "yes":
            st.chat_message("user").markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            try:
                st.session_state.name = prompt
                response = "Please verify, is your name " + prompt + "?"
            except Exception as e:
                response = str(e)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        elif prompt == "yes":
            st.chat_message("user").markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            try:
                response = (
                    "Great, your name is "
                    + st.session_state.name
                    + ", please give me your email address."
                )
            except Exception as e:
                response = str(e)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
