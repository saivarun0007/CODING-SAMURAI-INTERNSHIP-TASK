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

    def start(self):
        print("Welcome to the HelpDesk Assistant.")
        self.name = input("Before we begin, may I know your name? : ")
        print(f"Hello {self.name}, how can I assist you today?")
        
        while True:
            user_input = input(f"{self.name}: ").lower().strip()
            if self.check_exit(user_input):
                print("Thank you for chatting. Goodbye!")
                break
            
            intent = self.identify_intent(user_input)
            self.respond(intent)

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
            self.respond_product_info()
        elif intent == 'tech_support':
            self.respond_tech_support()
        elif intent == 'returns':
            self.respond_returns()
        elif intent == 'general_help':
            self.respond_general_help()
        else:
            self.respond_unknown()

    def respond_product_info(self):
        responses = [
            "Our product line includes the latest models with top-tier specifications.",
            "You can explore detailed product information on our website under the 'Products' section.",
            "Most of our products are reviewed highly by users for reliability and value.",
        ]
        print(random.choice(responses))

    def respond_tech_support(self):
        responses = [
            "Please describe the issue you're facing. We'll do our best to assist.",
            "For immediate assistance, you may also contact our technical support hotline.",
            "Try restarting the device first—many issues are resolved that way.",
        ]
        print(random.choice(responses))

    def respond_returns(self):
        responses = [
            "You may return products within 30 days of purchase with the receipt.",
            "Please make sure the product is in original condition when requesting a return.",
            "Our return center operates Monday to Friday from 10 AM to 6 PM.",
        ]
        print(random.choice(responses))

    def respond_general_help(self):
        responses = [
            "I'm here to help! Ask me about products, technical issues, or return policies.",
            "Sure, please let me know what you need help with.",
            "Our support team can assist with product guidance, orders, and more.",
        ]
        print(random.choice(responses))

    def respond_unknown(self):
        responses = [
            "I'm not sure I understand. Could you rephrase your question?",
            "Apologies, I couldn't recognize your request. Try asking about product info, returns, or support.",
            "That's a bit unclear. Could you please clarify?",
        ]
        print(random.choice(responses))

# Run the chatbot
if __name__ == "__main__":
    bot = HelpDeskBot()
    bot.start()
