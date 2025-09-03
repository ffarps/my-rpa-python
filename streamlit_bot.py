import streamlit as st
import gc
import random
import string
from define_type_of_flow import define_type_of_flow
from modular01 import ChatbotState

# Define greeting keywords and responses
greetings = [
    "hello",
    "hi",
    "hey",
    "greetings",
    "what's up",
    "good morning",
    "good afternoon",
    "good evening",
]
responses = ["Hello!", "Hi there!", "Hey!", "Greetings!", "How can I assist you today?"]
# Define check-in keywords and responses
checkins = ["check", "in", "checkin"]
checkin_responses = [
    "For checking in, please provide your Name. Thank you!",
    "I will check in with you, please give me your Name. Thank you!",
    "Let's get you checked in. What's your name?",
]

# Initialize session state variables
if "type_of_flow" not in st.session_state:
    st.session_state.type_of_flow = "None"
if "custom_flow" not in st.session_state:
    st.session_state.custom_flow = False
if "chat_state" not in st.session_state:
    st.session_state.chat_state = ChatbotState.ASK_NAME


# Function to reset the chat session state
def reset_chat():
    st.session_state.messages = []
    st.session_state.context = None
    st.session_state.custom_flow = False  # Reset custom flow state
    st.session_state.type_of_flow = "None"  # Reset type of flow
    st.session_state.chat_state = ChatbotState.ASK_NAME
    gc.collect()


# Preprocess user input text for better keyword matching
def preprocess_text_before_sending_to_gpt(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()
    return tokens


# Generate a response based on user input keywords
def generate_response_from(user_input):
    tokens = preprocess_text_before_sending_to_gpt(user_input)
    if any(token in greetings for token in tokens):
        return random.choice(responses)
    elif "check" in tokens and ("in" in tokens or "checkin" in tokens):
        st.session_state.custom_flow = True
        st.session_state.type_of_flow = "checkin"
        return random.choice(checkin_responses)

    return "I'm here to help, but I don't have the answer to that."


# Main function to run the Streamlit chatbot interface
def simplebot():
    # Sidebar
    with st.sidebar:
        st.title("ℹ️ About")
        st.markdown(
            "This is a simple virtual assistant chatbot for greetings and check-ins."
        )
        st.markdown("**Features:**")
        st.markdown("- Greeting responses")
        st.markdown("- Check-in process")
        st.button("🔄 Reset Chat", on_click=reset_chat)

    # Custom CSS for better styling
    st.markdown(
        """
    <style>
    [data-testid="stChatMessage"] {
        background-color: #f8f9fa;
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stChatInput {
        border-radius: 20px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.title("🤖 Simple Check-in Virtual Assistant Bot")
    st.markdown("### Welcome! 👋")
    st.markdown(
        "Start by greeting me or saying 'check in' to begin the check-in process."
    )
    st.caption(
        f"`Type of flow: {st.session_state.type_of_flow} | Custom flow: {st.session_state.custom_flow} `"
    )
    if "messages" not in st.session_state:
        st.session_state.messages = []
        reset_chat()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Help section
    with st.expander("ℹ️ Help & Instructions"):
        st.markdown("**How to use:**")
        st.markdown("- Say hello, hi, or greetings for a friendly response")
        st.markdown("- Say 'check in' to start the check-in process")
        st.markdown("- The bot will guide you through the check-in")

    if not st.session_state.custom_flow:
        if prompt := st.chat_input("Type your message here..."):
            if prompt.strip():  # Validate input is not empty or whitespace
                st.chat_message("user").markdown(prompt)
                st.session_state.messages.append({"role": "user", "content": prompt})
                try:
                    response = generate_response_from(prompt)
                except Exception as e:
                    response = "Sorry, an error occurred. Please try again."
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.rerun()
    else:
        if st.session_state.chat_state != ChatbotState.DONE:
            define_type_of_flow(st.session_state.type_of_flow)
    st.button("Clear Chat", on_click=reset_chat)


simplebot()
