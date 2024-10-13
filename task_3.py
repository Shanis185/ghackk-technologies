
import nltk
from nltk.tokenize import word_tokenize


nltk.download('punkt')  
nltk.download('punkt_tab')

# Define a simple set of responses for the chatbot
responses = {
    "about": "Castle Swimmer is a fantasy webcomic about a swimmer who discovers a new world and embarks on adventures while uncovering prophecies.",
    "main characters": "The main characters include the swimmer, who is central to the story, and various allies and antagonists they meet along the way.",
    "prophecy": "The new prophecy unveiled in chapters 83-89 is significant to the swimmer's journey and their role in the world.",
    "adventures": "The swimmer encounters many challenges and mysteries in their quest, often facing powerful foes and uncovering hidden truths.",
    "world": "The story is set in a vibrant underwater world filled with magic, danger, and unexpected allies."
}

# Function to respond based on user input
def chatbot_response(user_input):
    # Tokenize user input
    tokens = word_tokenize(user_input.lower())
    
    # Check for keywords and respond accordingly
    if "about" in tokens:
        return responses["about"]
    elif "main" in tokens and "characters" in tokens:
        return responses["main characters"]
    elif "prophecy" in tokens:
        return responses["prophecy"]
    elif "adventures" in tokens:
        return responses["adventures"]
    elif "world" in tokens:
        return responses["world"]
    else:
        return "I'm sorry, I don't have an answer for that. Can you ask something else?"

# Main loop for the chatbot
def main():
    print("Welcome to the Castle Swimmer Chatbot! Ask me anything about the comic.")
    print("Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Enjoy reading Castle Swimmer!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    main()
