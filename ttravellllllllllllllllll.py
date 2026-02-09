import random

def travel_chatbot():
    print("Welcome to TravelBot! 🌍 Ask me anything about travel.")

    # Jokes and tips
    jokes = [
        "Why did the tourist bring a ladder? Because they wanted to reach new heights!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What did one ocean say to the other? Nothing, they just waved!"
    ]

    tips = [
        "Always keep a copy of your passport and travel insurance!",
        "Pack light and bring only essentials to make your travels easier.",
        "Try to learn a few words of the local language; it goes a long way!"
    ]

    destinations = [
        "Mexico City", 
        "Tokyo", 
        "Paris", 
        "Cape Town", 
        "Machu Picchu"
    ]

    # Trivia questions
    trivia_questions = [
        ("What is the capital of France?", "paris"),
        ("Which continent is known as the 'Dark Continent'?", "africa"),
        ("What is the largest ocean on Earth?", "pacific")
    ]

    while True:
        user_input = input("You: ").lower()

        if "quit" in user_input or "exit" in user_input:
            print("TravelBot: Have a great day! Safe travels! ✈️")
            break
        
        elif "destination" in user_input:
            print("TravelBot: How about visiting " + random.choice(destinations) + "?")

        elif "tip" in user_input:
            print("TravelBot: " + random.choice(tips))

        elif "joke" in user_input:
            print("TravelBot: " + random.choice(jokes))

        elif "game" in user_input or "trivia" in user_input:
            question, answer = random.choice(trivia_questions)
            print(f"TravelBot: Here's a trivia question for you: {question}")
            user_answer = input("Your answer: ").lower()
            if user_answer == answer:
                print("TravelBot: Correct! 🎉")
            else:
                print(f"TravelBot: Wrong! The correct answer is {answer.capitalize()}.")

        else:
            print("TravelBot: I'm not sure about that. Can you ask something else?")

# Start the chatbot
travel_chatbot()
