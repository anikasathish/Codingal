amount = int(input("enter an amount please !"))
notes100= amount//100
notes50= (amount%100)//50
notes10= ((amount%100)%50)//10
print("the number of notes of 100$:",notes100)
print("the number of notes of 50$:", notes50)
print("the number of notes of 10$:", notes10)
