print("what type of ride would you like ??")
print("1. Bike")
print("2. Car")
choice = int(input("pick a number, 1 or 2"))

if choice == 1:
    print("what type of bike would you like")
    print("1. Scooter")
    print("2. Scooty")
    choice2 = int(input("pick a number, 1 or 2"))
    if choice2 == 1:
        print("you have selected scooter")
    else:
        print("you have selected scooty")
elif choice == 2:
    print("what type of car would you like???")
    print("1. Sedan")
    print("2. SUV")
    choice3 = int(input("pick a number, 1 or 2"))
    if choice3 == 1:
        print("you have selected sedan")
    else:
        print("you have selected suv")

else:
    print("wrong choice !")