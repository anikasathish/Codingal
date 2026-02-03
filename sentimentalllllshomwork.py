positive_words = ["good", "happy", "love", "great"]
negative_words = ["bad", "sad", "hate", "angry"]

positive = 0
negative = 0
neutral = 0

print("Simple Sentiment Chatbot")
print("Type 'stats' to see results or 'exit' to quit")

while True:
    text = input("\nYou: ").lower()

    if text == "exit":
        print("\nFinal Report:")
        print("Positive:", positive)
        print("Negative:", negative)
        print("Neutral:", neutral)
        print("Goodbye!")
        break

    elif text == "stats":
        print("\nCurrent Stats:")
        print("Positive:", positive)
        print("Negative:", negative)
        print("Neutral:", neutral)

    else:
        if any(word in text for word in positive_words):
            positive += 1
            print("Bot: That sounds positive 🙂")
        elif any(word in text for word in negative_words):
            negative += 1
            print("Bot: That sounds negative 🙁")
        else:
            neutral += 1
            print("Bot: That sounds neutral 😐")
