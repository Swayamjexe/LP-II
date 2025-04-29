# import nltk
# from nltk.tokenize import word_tokenize
# nltk.download('punkt')
# nltk.download('punkt_tab')

# # Define simple responses
# responses = {
#     "ai": "AI stands for Artificial Intelligence. It's about making machines think and act like humans.",
#     "machine-learning": "Machine Learning is a subset of AI that helps machines learn from data.",
#     "deep-learning": "Deep Learning is a type of Machine Learning using multi-layered neural networks.",
#     "types of systems": "There are 3 types: Narrow AI, General AI, and Superintelligent AI.",
#     "natural language processing": "NLP helps machines understand and respond in human language."
# }

# def get_response(user_input):
#     tokens = word_tokenize(user_input.lower())
#     for keyword in responses:
#         if any(word in keyword for word in tokens):
#             return responses[keyword]
#     return "I'm not sure about that. Ask me something else about AI."

# def ai_chatbot():
#     print("Hi! I'm your AI chatbot. Ask me something about AI. (type 'quit' to stop)")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit", "exit"]:
#             print("Chatbot: Bye!")
#             break
#         response = get_response(user_input)
#         print(f"Chatbot: {response}")

# # Run it
# ai_chatbot()




import tkinter as tk
from tkinter import scrolledtext
import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('punkt')

# Define simple responses
responses = {
    "ai": "AI stands for Artificial Intelligence. It's about making machines think and act like humans.",
    "machine-learning": "Machine Learning is a subset of AI that helps machines learn from data.",
    "deep-learning": "Deep Learning is a type of Machine Learning using multi-layered neural networks.",
    "types of systems": "There are 3 types: Narrow AI, General AI, and Superintelligent AI.",
    "natural language processing": "NLP helps machines understand and respond in human language."
}

def get_response(user_input):
    tokens = word_tokenize(user_input.lower())
    for keyword in responses:
        if any(word in keyword for word in tokens):
            return responses[keyword]
    return "I'm not sure about that. Ask me something else about AI."

# GUI Code
def send_message():
    user_input = entry.get()
    if user_input.strip() != "":
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        response = get_response(user_input)
        chat_window.insert(tk.END, "Chatbot: " + response + "\n\n")
        chat_window.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        chat_window.yview(tk.END)  # Auto-scroll to the bottom

# Main window
root = tk.Tk()
root.title("Simple AI Chatbot")

# Chat display area
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, width=60, height=20)
chat_window.pack(padx=10, pady=10)

# User input field
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=(0,10), side=tk.LEFT, expand=True)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=(0,10), pady=(0,10), side=tk.RIGHT)

root.mainloop()
