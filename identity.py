x = 5
if type(x) is int:
    print ("true !")
else:
    print("false !")
y = 2.0
if type(y) is not float:
    print("true !")
else:
    print("false !")
a = 20
b = 20
c = 25
if a is b:
    print("a and b are same identity !")
if a is not c:
    print("a and c have different identities !")
    