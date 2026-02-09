import re, random
from colorama import Fore, init
init(autoreset = True)
destinations = {
    "beaches": ["Bali", "Maldives", "Hawaii"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Paris", "New York", "Tokyo"]
}

jokes = [
    "Why dont programmers like nature? It has too many bugs.",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all of their hot spots!"
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())
def reccomend():
    print(Fore.CYAN + "Travel Bot: Beaches, mountains, or cities? ")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"Travel Bot: How about visiting {suggestion}?")
        print(Fore.CYAN + "Travel Bot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"Travel Bot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "Travel Bot: No worries! Let's try another suggestion.")
            reccomend()
        else:
            print(Fore.RED + "Travel Bot: I'll try another suggestion.")
            reccomend()
    else:
        print(Fore.RED + "Travel Bot: Sorry, I don't have that kind of destination.")
        reccomend()
    
def packing_tips():
    print(Fore.CYAN + "Travel Bot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + f"Travel Bot: For how long?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"Travel Bot: Tips for a trip to {location} for {days} days:")
    print(Fore.GREEN + "- Pack light and versatile clothing.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

def tell_joke():
    print(Fore.YELLOW + f"Travel Bot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots(say reccomendation)")
    print(Fore.GREEN + "- Give packing tips(say packing)")
    print(Fore.GREEN + "- Tell a joke(say joke)")

    print(Fore.CYAN + "type 'exit' or 'bye' to end\n ")

def chat():
    print(Fore.CYAN + "Travel Bot: Hello! I'm Travel Bot! ")
    name = input(Fore.YELLOW + "Travel Bot: What's your name? ")
    print(Fore.GREEN + f"Travel Bot: Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "reccomend" in user_input or "suggest" in user_input:
            reccomend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + f"Travel Bot: Goodbye, {name}! Safe travels!")
            break
        else:
            print(Fore.RED + "Travel Bot: Could you rephrase that?")
    
if __name__ == "__main__":
    chat()

    