try:
    number = int(input("Enter a number: "))
    print(f"The number you entered is: {number}")

except ValueError as ex:
    print("Exception:", ex)
    
