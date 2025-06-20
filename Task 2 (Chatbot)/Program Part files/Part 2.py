import tkinter as tk
from tkinter import scrolledtext
import random

class HelpDeskBot:
    def __init__(self):
        self.name = ""
        self.exit_commands = ['exit', 'bye', 'quit', 'close']
        self.negative_responses = ['no', 'nope', 'nah', 'not really', 'never']
        self.commands = {
            'product_info': ['product', 'details', 'specs'],
            'tech_support': ['support', 'issue', 'error', 'problem'],
            'returns': ['return', 'refund', 'exchange'],
            'general_help': ['help', 'assist', 'question'],
        }

    def check_exit(self, user_input):
        for exit_word in self.exit_commands:
            if exit_word in user_input:
                return True
        return False

    def identify_intent(self, user_input):
        for intent, keywords in self.commands.items():
            for keyword in keywords:
                if keyword in user_input:
                    return intent
        return 'unknown'

    def respond(self, intent):
        if intent == 'product_info':
            return random.choice([
                "Our product line includes the latest models with top-tier specifications.",
                "You can explore detailed product information on our website under the 'Products' section.",
                "Most of our products are reviewed highly by users for reliability and value.",
            ])
        elif intent == 'tech_support':
            return random.choice([
                "Please describe the issue you're facing. We'll do our best to assist.",
                "For immediate assistance, you may also contact our technical support hotline.",
                "Try restarting the device first—many issues are resolved that way.",
            ])
        elif intent == 'returns':
            return random.choice([
                "You may return products within 30 days of purchase with the receipt.",
                "Please make sure the product is in original condition when requesting a return.",
                "Our return center operates Monday to Friday from 10 AM to 6 PM.",
            ])
        elif intent == 'general_help':
            return random.choice([
                "I'm here to help! Ask me about products, technical issues, or return policies.",
                "Sure, please let me know what you need help with.",
                "Our support team can assist with product guidance, orders, and more.",
            ])
        else:
            return random.choice([
                "I'm not sure I understand. Could you rephrase your question?",
                "Apologies, I couldn't recognize your request. Try asking about product info, returns, or support.",
                "That's a bit unclear. Could you please clarify?",
            ])

# GUI Chat Interface using Tkinter
class ChatGUI:
    def __init__(self, root):
        self.bot = HelpDeskBot()

        self.root = root
        self.root.title("𝐂𝐨𝐝𝐢𝐧𝐠 𝐒𝐚𝐦𝐮𝐫𝐚𝐢 𝐈𝐧𝐭𝐞𝐫𝐧 Chatbot")
        self.root.geometry("500x600")

        # Chat Display Area
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
        self.chat_area.config(state='disabled')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Entry for user message
        self.entry_field = tk.Entry(root, font=("Arial", 14))
        self.entry_field.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.entry_field.bind("<Return>", self.send_message)

        # Welcome and name prompt
        self.ask_name()

    def ask_name(self):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, "Bot: Welcome to the HelpDesk Assistant.\n")
        self.chat_area.insert(tk.END, "Bot: Before we begin, may I know your name?\n")
        self.chat_area.config(state='disabled')

    def send_message(self, event):
        user_input = self.entry_field.get().strip()
        self.entry_field.delete(0, tk.END)

        if not user_input:
            return

        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"You: {user_input}\n")

        # Initial name handling
        if self.bot.name == "":
            self.bot.name = user_input
            self.chat_area.insert(tk.END, f"Bot: Hello {self.bot.name}, how can I assist you today?\n")
        elif self.bot.check_exit(user_input.lower()):
            self.chat_area.insert(tk.END, "Bot: Thank you for chatting. Goodbye!\n")
            self.chat_area.config(state='disabled')
            self.root.after(2000, self.root.destroy)  # auto close after 2 sec
        else:
            intent = self.bot.identify_intent(user_input.lower())
            response = self.bot.respond(intent)
            self.chat_area.insert(tk.END, f"Bot: {response}\n")

        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)  # auto-scroll

# Launch GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatGUI(root)
    root.mainloop()
