# main.py

from etl.load import prepare_documents
from chatbot.rag_chatbot import RAGChatbot

def main():
    print("🔄 Loading documents...")
    documents = prepare_documents("data")

    print(f"📄 Loaded {len(documents)} text chunks.")

    print("⚙️ Initializing RAG chatbot...")
    chatbot = RAGChatbot(documents)

    print("✅ RAG Chatbot is ready!")
    print("Ask anything based on your documents. Type 'exit' to quit.\n")

    while True:
        user_query = input("You: ")

        if user_query.lower() == "exit":
            print("Goodbye! 👋")
            break

        response = chatbot.ask(user_query)
        print("\nBot:", response, "\n")


if __name__ == "__main__":
    main()
