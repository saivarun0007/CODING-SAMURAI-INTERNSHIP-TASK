import tkinter as tk
from tkinter import scrolledtext, messagebox
import random
import os
import datetime
import pyttsx3
import speech_recognition as sr
import threading

#  Voice Setup 
engine = pyttsx3.init()
engine.setProperty('rate', 170)
recognizer = sr.Recognizer()

def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run, daemon=True).start()

def get_voice_input():
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
    except:
        return ""

#  ChatBot Logic 
class HelpDeskBot:
    def __init__(self):
        self.name = ""
        self.exit_commands = ['exit', 'bye', 'quit', 'close']
        self.commands = {
            'product_info': ['product', 'details', 'specs'],
            'tech_support': ['support', 'issue', 'error', 'problem'],
            'returns': ['return', 'refund', 'exchange'],
            'general_help': ['help', 'assist', 'question'],
        }

    def check_exit(self, user_input):
        return any(word in user_input for word in self.exit_commands)

    def identify_intent(self, user_input):
        for intent, keywords in self.commands.items():
            for keyword in keywords:
                if keyword in user_input:
                    return intent
        return 'unknown'

    def respond(self, intent):
        responses = {
            'product_info': [
                "Our product line includes the latest models with top-tier specifications.",
                "You can explore detailed product information on our website under the 'Products' section.",
                "Most of our products are reviewed highly by users for reliability and value.",
            ],
            'tech_support': [
                "Please describe the issue you're facing. We'll do our best to assist.",
                "For immediate assistance, you may also contact our technical support hotline.",
                "Try restarting the device first—many issues are resolved that way.",
            ],
            'returns': [
                "You may return products within 30 days of purchase with the receipt.",
                "Please make sure the product is in original condition when requesting a return.",
                "Our return center operates Monday to Friday from 10 AM to 6 PM.",
            ],
            'general_help': [
                "I'm here to help! Ask me about products, technical issues, or return policies.",
                "Sure, please let me know what you need help with.",
                "Our support team can assist with product guidance, orders, and more.",
            ],
            'unknown': [
                "I'm not sure I understand. Could you rephrase your question?",
                "Apologies, I couldn't recognize your request. Try asking about product info, returns, or support.",
                "That's a bit unclear. Could you please clarify?",
            ]
        }
        return random.choice(responses[intent])

#  GUI Application 
class HelpDeskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("𝐂𝐨𝐝𝐢𝐧𝐠 𝐒𝐚𝐦𝐮𝐫𝐚𝐢 𝐈𝐧𝐭𝐞𝐫𝐧 Chatbot")
        self.root.geometry("700x600")
        self.root.configure(bg="#14A3C7")
        self.bot = HelpDeskBot()
        self.username = ""
        self.chat_log_path = "chat_logs.txt"

        self.create_login_page()

    def create_login_page(self):
        self.clear_window()
        self.label = tk.Label(self.root, text="Login to HelpDesk", font=("Arial", 18, 'bold'), fg="black", bg="#14A3C7")
        self.label.pack(pady=20)

        self.name_entry = tk.Entry(self.root, font=("Arial", 14), fg="gray")
        self.name_entry.insert(0, "Enter your name")
        self.name_entry.bind("<FocusIn>", self.clear_placeholder)
        self.name_entry.bind("<FocusOut>", self.restore_placeholder)
        self.name_entry.pack(pady=10)

        self.login_btn = tk.Button(self.root, text="Login", command=self.login, font=("Arial", 12), bg="#333", fg="white")
        self.login_btn.pack(pady=10)

    def clear_placeholder(self, event):
        if self.name_entry.get() == "Enter your name":
            self.name_entry.delete(0, tk.END)
            self.name_entry.config(fg="black")

    def restore_placeholder(self, event):
        if not self.name_entry.get():
            self.name_entry.insert(0, "Enter your name")
            self.name_entry.config(fg="gray")

    def login(self):
        name = self.name_entry.get().strip()
        if name and name != "Enter your name":
            self.bot.name = name
            self.username = name
            self.create_chat_page()
        else:
            messagebox.showwarning("Input Error", "Please enter your name to continue.")

    def create_chat_page(self):
        self.clear_window()

        # Menu bar
        menu_frame = tk.Frame(self.root, bg="#1e1e1e")
        menu_frame.pack(fill=tk.X)
        tk.Button(menu_frame, text="History", command=self.show_history, bg="#333", fg="white").pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(menu_frame, text="Logout", command=self.create_login_page, bg="#333", fg="white").pack(side=tk.RIGHT, padx=5, pady=5)

        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Arial", 12), bg="#2e2e2e", fg="white")
        self.chat_area.config(state='disabled')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_field = tk.Entry(self.root, font=("Arial", 14), bg="#3e3e3e", fg="white")
        self.entry_field.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.entry_field.bind("<Return>", self.send_message)

        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Send", command=self.send_message, bg="#4e4e4e", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="🎤 Speak", command=self.voice_input, bg="#4e4e4e", fg="white", width=10).pack(side=tk.LEFT, padx=5)

        self.bot_intro()

    def bot_intro(self):
        self.add_chat("Bot", f"Hello {self.username}, how can I assist you today?")

    def send_message(self, event=None):
        user_input = self.entry_field.get().strip()
        self.entry_field.delete(0, tk.END)
        if not user_input:
            return

        self.add_chat("You", user_input)

        if self.bot.check_exit(user_input.lower()):
            self.add_chat("Bot", "Thank you for chatting. Goodbye!")
            speak("Thank you for chatting. Goodbye!")
            self.root.after(2000, self.root.destroy)
            return

        intent = self.bot.identify_intent(user_input.lower())
        response = self.bot.respond(intent)
        self.add_chat("Bot", response)
        speak(response)

    def voice_input(self):
        self.add_chat("System", "Listening...")
        user_input = get_voice_input()
        if user_input:
            self.entry_field.insert(0, user_input)
            self.send_message()
        else:
            self.add_chat("System", "Sorry, couldn't hear you.")

    def add_chat(self, sender, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)
        self.save_log(sender, message)

    def save_log(self, sender, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] {sender} ({self.username}): {message}\n"
        with open(self.chat_log_path, "a") as f:
            f.write(log_line)

    def show_history(self):
        if not os.path.exists(self.chat_log_path):
            messagebox.showinfo("History", "No chat history found.")
            return

        history_win = tk.Toplevel(self.root)
        history_win.title("Chat History")
        history_win.geometry("600x400")
        history_win.configure(bg="#1e1e1e")

        text_area = scrolledtext.ScrolledText(history_win, wrap=tk.WORD, font=("Arial", 12), bg="#2e2e2e", fg="white")
        text_area.pack(fill=tk.BOTH, expand=True)

        with open(self.chat_log_path, "r") as f:
            logs = f.read()
            text_area.insert(tk.END, logs)
        text_area.config(state='disabled')

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

#  Run Application 
if __name__ == "__main__":
    root = tk.Tk()
    app = HelpDeskApp(root)
    root.mainloop()
