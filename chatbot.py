print("Hello! I am ChatBuddy 🤖. Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ").lower().strip()  

    if user_input == "exit":
        print("ChatBuddy: Goodbye! Have a great day! 👋")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("ChatBuddy: Hello there! How can I help you today?")

    elif "how are you" in user_input:
        print("ChatBuddy: I'm doing great! Thanks for asking. How about you?")

    elif "your name" in user_input:
        print("ChatBuddy: I'm ChatBuddy, your friendly chatbot!")

    elif "weather" in user_input:
        print("ChatBuddy: I can't check the weather yet, but it's always sunny in my world! ☀")

    elif "bye" in user_input:
        print("ChatBuddy: Bye! Come back soon. 👋")
        break

    else:
        print("ChatBuddy: Hmm... I don't understand that yet. 🤔")
