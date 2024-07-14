def respond(input_text):
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm a bot, I'm always good!",
        "bye": "Goodbye!"
    }
    
    input_text = input_text.lower()
    return responses.get(input_text, "I don't understand that.")

if __name__ == "__main__":
    print("Welcome to Hello-World-Bot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        response = respond(user_input)
        print(f"Bot: {response}")
