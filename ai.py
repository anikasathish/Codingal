print("Hello, I am AI Chatbot. What's your name?:")

name = input()

print("Nice to meet you, ", name)

print("How are you feeling today? (good/bad):")

mood = input().lower()


if mood == "good":
    print("I'm so happy to hear that, ", name, "!")
elif mood == "bad":
    print("I'm sorry to hear that, ", name, ". I hope things get better soon!")
else:
    print("I see. Sometimes feelings are hard to describe.")

print("It was nice chatting with you, now goodbye!")

