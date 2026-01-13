num = int(input("Enter the Number:"))
t = num
NumLen = 0


while t > 0:
    NumLen = NumLen + 1
    t = int(t/10)

if NumLen>=4:
    NumLen = int(NumLen/2)
    chk = 0
    while num>0:
        rem = num%10
        if chk== NumLen:
            midOne = rem
        elif chk == ( NumLen - 1):
            midTwo = rem
        num = int(num/10)
        chk = chk + 1
    prod = midOne*midTwo 
    print("\nProduct of Mid Digits("+str(midOne)+"*"+str(midTwo)+")=", prod)
else:
    print("\nIt's not a 4 or more than 4 digit number")

