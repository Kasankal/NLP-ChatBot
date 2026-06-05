print("Welcome to Student Help Chatbot")

while True:
    user = input("You: ")

    if "hello" in user.lower():
        print("Bot: Hello Student")

    elif "exam" in user.lower():
        print("Bot: CAT 1 starts next week")

    elif "bye" in user.lower():
        print("Bot: Goodbye")
        break

    else:
        print("Bot: I do not understand")
