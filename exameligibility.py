medicalcause = str(input("do you have a medical cause? if so, type yes. else, type no."))

if medicalcause == "yes":
    print("you can take the exam")
else:
    attendance = int(input("enter your attendance score"))
    if attendance >= 75:
        print("yes, you can take the exam")
    else:
        print("sorry, you cannot take the exam")
