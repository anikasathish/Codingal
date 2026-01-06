string = input("Please enter your own string:")

string2 = ('')

for i in string:
    string2 = i + string2

print("\nThe Original string is:", string)

print("\nThe Reversed string is:", string2)