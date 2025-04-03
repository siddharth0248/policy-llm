from app.chatbot import Chatbot

if __name__ == "__main__":
    chatbot = Chatbot()
    while True:
        query = input("Ask your question: ")
        if query.lower() == "exit":
            break
        response = chatbot.ask(query)
        print(f"Response: {response}")
