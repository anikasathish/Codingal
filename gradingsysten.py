print("enter the marks you obtained in these 5 subjects")

math = int(input("enter your math input :"))
science = int(input("enter your science input:"))
english = int(input("enter your english input:"))
history = int(input("enter your history input:"))
music = int(input("enter your music input:"))

total = math + science + history + english + music

avg = total / 5

print("average =", avg)

if avg >= 91 and avg <= 100:
    print(" your grade is A1")

elif avg >= 81 and avg < 91:
    print(" your grade is A2")

elif avg >= 71 and avg < 81:
    print("your grade is B1")

elif avg >= 61 and avg < 71:
    print("your grade is B2")

elif avg >= 51 and avg <61:
    print("your grade is C1")

elif avg >= 41 and avg <51:
    print("your grade is C2")

elif  avg >= 33 and avg <41:
    print("your grade is D")

elif avg >= 21 and avg <33:
    print("your grade is E1")

elif avg >= 0 and avg < 21:
    print("your grade is E2")

else:
    print(" invalid input")
