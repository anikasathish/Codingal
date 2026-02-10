import random

print("Welcome to Rock, Paper, Scissors!")
user_choice = input("Enter 'r' for rock, 'p' for paper, and 's' for scissors: ")
computer_choice = random.choice(['r', 'p', 's'])

print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'r' and computer_choice == 's') or \
     (user_choice == 'p' and computer_choice == 'r') or \
     (user_choice == 's' and computer_choice == 'p'):
    print("You win!")
else:
    print("You lose!")
