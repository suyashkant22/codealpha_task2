# codealpha_task2
A simple rule-based chatbot in Python that replies to greetings and goodbyes using if-elif, functions, loops and input/output.
# Basic Chatbot

A simple rule-based chatbot written in Python. It reads what the user types and replies with predefined responses.

## Features

- Responds to greetings, a "how are you" question and goodbyes
- Ignores letter case and extra spaces in the input
- Keeps chatting in a loop until the user says goodbye
- Gives a helpful message when it doesn't understand the input

## Concepts Used

- `if-elif-else` statements
- Functions
- Loops (`while`)
- Input / output (`input()` and `print()`)

## How to Run

Make sure Python 3 is installed, then run:

```bash
python chatbot.py
```

## Sample Conversation

```
Chatbot: Hello! Type 'bye' to end the chat.
You: hello
Chatbot: Hi!
You: how are you
Chatbot: I'm fine, thanks!
You: bye
Chatbot: Goodbye!
```

## Supported Inputs

| User input             | Chatbot reply                 |
|------------------------|-------------------------------|
| `hello`, `hi`, `hey`   | Hi!                           |
| `how are you`          | I'm fine, thanks!             |
| `bye`, `goodbye`, `exit` | Goodbye!                    |
| anything else          | Sorry, I didn't understand... |

## Files

- `chatbot.py` – the chatbot program
- `README.md` – project description
- 
