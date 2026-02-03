import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}Welcome to the Sentiment Spy!{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL} ").strip()

if not user_name:

    user_name = "Mystery Agent"  

conversation_history = []

while True:

    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:

        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "exit":

        print(f"\n{Fore.BLUE}???? Exiting Sentiment Spy. Farewell, Agent {user_name}! ????{Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}Conversation history cleared.{Style.RESET_ALL}")
    for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, 1):
        if sentiment_type == "positive":
            color = Fore.GREEN
            emoji = "😊"
        elif sentiment_type == "negative":
            color = Fore.RED
            emoji = "😞"
        else:
            color = Fore.YELLOW
            emoji = "😐"
        print(f"{idx}. {color}{emoji}{text} (Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
    continue
polarity = TextBlob(user_input).sentiment.polarity
if polarity > 0.25:
    sentiment_type = "positive"
    emoji = "😊"
    color = Fore.GREEN
elif polarity < -0.25:
    sentiment_type = "negative"
    emoji = "😞"
    color = Fore.RED
else:
    sentiment_type = "neutral"
    emoji = "😐"
    color = Fore.YELLOW
conversation_history.append((user_input, polarity, sentiment_type))

print(f"{color}{emoji} Sentiment: {sentiment_type.capitalize()} (Polarity: {polarity:.2f}){Style.RESET_ALL}")
