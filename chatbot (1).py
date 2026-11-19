"""Basic Rule-Based Chatbot
Concepts used: if-elif, functions, loops, input/output
"""


def get_reply(user_input):
    """Return a predefined reply based on the user's message."""
    message = user_input.strip().lower()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message in ("how are you", "how are you?"):
        return "I'm fine, thanks!"
    elif message in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that. Try 'hello', 'how are you' or 'bye'."


def chatbot():
    """Run the chat loop until the user says bye."""
    print("Chatbot: Hello! Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Chatbot:", reply)

        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    chatbot()
