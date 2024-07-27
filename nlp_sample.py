import random
import string

# Sample data
greetings = ["hello", "hi", "hey", "greetings", "what's up"]
responses = ["Hello!", "Hi there!", "Hey!", "Greetings!", "What's up?"]


# Preprocessing functions
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Split into words (tokens)
    tokens = text.split()
    return tokens


# Function to respond based on greetings
def get_response(user_input):
    user_tokens = preprocess_text(user_input)
    for token in user_tokens:
        if token in greetings:
            return random.choice(responses)
    return "I'm sorry, I didn't understand that."


# Function to handle conversation
def handle_conversation():
    print("Chatbot: Hi! How can I help you? Type 'quit' to exit.")
    user_input = input("You: ")
    while user_input.lower() != "quit":
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        user_input = input("You: ")
    print("Chatbot: Goodbye!")


# Start the conversation
handle_conversation()
