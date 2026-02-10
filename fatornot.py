import random

# Your name
name = input("Enter your name: ")

# Ask for the key people
ex_name = input("Enter an ex's name: ")
ex_bsf_name = input("Enter an ex-best friend's name: ")
crush_name = input("Enter your crush's name: ")
bsf_name = input("Enter your best friend's name: ")
mom_name = input("Enter your mom's name: ")
dad_name = input("Enter your dad's name: ")
teacher_name = input("Enter a teacher's name: ")
random_girl_name = input("Enter a random girl's name: ")
random_boy_name = input("Enter a random boy's name: ")

# Drama categories
boys_drama = [
    f"{crush_name} likes you… but they’re also talking to someone else 😳",
    f"A message from {crush_name} could totally change your day!",
    f"That mysterious look from {crush_name}? Totally intentional 😏",
    f"You might bump into {crush_name}… awkwardly cute moment incoming!",
    f"{random_boy_name} is pretending not to notice you… but they totally do."
]

bsf_drama = [
    f"Your bestie {bsf_name} might be a little salty today… but it’s nothing you can’t fix!",
    f"A small argument could happen with {bsf_name}… snacks fix everything.",
    f"{bsf_name} is planning a surprise for you… or maybe a harmless prank!",
    f"Someone might feel jealous of your friendship with {bsf_name}. Stay awesome together!",
    f"Drama alert: {ex_bsf_name} wants your opinion and it could start gossip!"
]

family_drama = [
    f"{mom_name} wants to talk to you about something important… or maybe just snacks 🍪",
    f"{dad_name} is suspiciously proud of you today 😏",
    f"{teacher_name} might give you extra credit… or extra homework!",
    f"{mom_name} and {dad_name} are plotting a surprise for you!",
]

random_drama = [
    f"{random_girl_name} just said something about you… time to stay fabulous!",
    f"{random_boy_name} is suddenly acting weird… pay attention!",
    f"Someone new might become your friend today… unexpected fun!",
]

advice = [
    "Always share snacks, it’s the ultimate peace treaty.",
    "Laugh at the small drama, it’s all temporary!",
    "Write down your secrets, not on social media!",
    "Smile at your crush… but don’t overthink it!",
    "Friendship > drama. Always.",
    "Sometimes staying out of drama is the juiciest move."
]

# Life score
life_score = (sum([ord(c) for c in name]) + random.randint(1, 50)) % 100

# Pick one from each category
boy_event = random.choice(boys_drama)
bsf_event = random.choice(bsf_drama)
family_event = random.choice(family_drama)
random_event = random.choice(random_drama)
tip = random.choice(advice)

# Print ultimate juicy life report
print(f"\n💖 Ultimate Middle School Life Report for {name} 💖")
print(f"Life Score: {life_score}/100\n")
print(f"💌 Boys Drama: {boy_event}")
print(f"👯 BFF Drama: {bsf_event}")
print(f"🏠 Family Drama: {family_event}")
print(f"🎲 Random Drama: {random_event}")
print(f"✨ Tip of the Day: {tip}")
