a = int(input("enter a speed:"))
b = int(input("enter b speed:"))
c = int(input("enter c speed:"))
avg = (a + b + c) / 3

print("your average speed is:", avg)

if avg > a and avg > b and avg > c:
    print(avg, "is higher than", a , b, "and", c)
elif avg > a and avg > b:
    print(avg,"is higher than", a, "and", b)
elif avg > b and avg > c:
    print(avg, "is higher than", b , "and", c)
elif avg > a and avg > c:
    print(avg, "is higher than", a, "and", c)
elif avg > a:
    print(avg, "is higher than", a)
elif avg > b:
    print(avg, "is higher than", b)
elif avg > c:
    print(avg, "is higher than ", c)
else:
    print("invalid input")
