print("Hi, My name is AI Chatbot. Pick one of the following games:")
print("1. Rock Paper Scissors")
print("2. Mad Libs")

choice = str(input("Enter 1 or 2: "))

if choice == '1':
    print("Welcome to Rock Paper Scissors!")

    print("Pick one: rock, paper, or scissors")
    user_choice = input("enter your choice:")
    if user_choice == 'rock':
        print("You chose rock.")
    elif user_choice == 'paper':
        print("You chose paper.")
    elif user_choice == 'scissors':
        print("You chose scissors.")
    else:
        print("Invalid choice. Please restart the program and select either rock, paper, or scissors.")

elif choice == '2':
    print("Welcome to Mad Libs!")
    color = input("Enter a color:")
    adjective = input("Enter an adjective:")
    name = input("Enter a name:")
    verb = input("Enter a verb:")
    noun = input("Enter a noun:")
    verb2 = input("Enter another verb:")
    verb3 = input("Enter one more verb:")
    noun2 = input("Enter another noun:")
    place = input("Enter a place:")
    print("Here is your Mad Libs story:")
    print(name, "was going to the", place, "when they arrived upon a", color, noun, "and they decieded to" \
    "watch the", noun, verb, "and it was a very", adjective, "sight to see. ")

else:
    print("Please restart the program and pick 1 or 2")


print("Thank you for playing, now would you like to chat with me? (yes/no)")
chatchoice = input().lower()

if chatchoice == "yes":
    print("Hello, I am AI Chatbot. What's your name?:")
    name = input()  
    print("Nice to meet you, ", name)
    print("How are you feeling today? (good/bad):")
    mood = input().lower()
    if mood == "good":
        print("I'm happy to hear that, ", name, "!")
    elif mood == "bad":
        print("I'm sorry to hear that, ", name, ". I hope things get better soon!")
    else: 
        print("I see. Sometimes feelings are hard to describe.")

print("Would you like to tell me your favorite subject? (yes/no)")
subjectchoice = input().lower()

if subjectchoice == "yes":
    print("What is your favorite subject?")
    subject = input()
    print("That's a great subject, ", name, "!")

print("Would you like to talk about who your friends are, or would you like to say goodbye?")

friendchoice = input("Type 'friends' to talk about friends or 'goodbye' to end the chat: ").lower()

if friendchoice == "friends":
    print("tell me who your closest friend is:")
    friend = input()
    print(friend, "sounds like a fun friend to have! What do you like to do together?")

    activity = input()
    print(activity, "sounds like a fun way to spend time with", friend, "!")
elif friendchoice == "goodbye":
    print("I had fun talking to you, ", name, ". Goodbye!")
else:
    print("Error in input. Please restart the program.")
print("Thank you for chatting with me, ", name, "! Have a great day!")