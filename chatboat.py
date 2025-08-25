import re

def chatbot():
    print("Chatbot: Hello! I'm ChatBuddy. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a nice day!")
            break

        # Rule-based responses
        elif re.search(r'\bhi\b|\bhello\b|\bhey\b', user_input):
            print("Chatbot: Hi there! How can I assist you?")
        
        elif re.search(r'\bhow are you\b', user_input):
            print("Chatbot: I'm just a bunch of code, but I'm doing great! Thanks for asking.")
        
        elif re.search(r'\bwhat is your name\b', user_input):
            print("Chatbot: My name is ChatBuddy!")
        
        elif re.search(r'\bhelp\b', user_input):
            print("Chatbot: Sure! I can answer questions like 'What is your name?', 'How are you?', or 'Tell me a joke'.")
        
        elif re.search(r'\btell me a joke\b', user_input):
            print("Chatbot: Why don't programmers like nature? It has too many bugs!")

        elif re.search(r'\bweather\b', user_input):
            print("Chatbot: I'm not connected to the internet, so I can't fetch the weather. Try asking your favorite weather app!")

        else:
            print("Chatbot: Sorry, I didn't understand that. Try asking something else or type 'help'.")

# Run the chatbot
chatbot()
