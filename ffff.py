# Class creation
class myClass:

# private variable
    _privateVar = 27;

    # private method
    def _privMeth(self):
        print("I'm inside class myClass")

# Function to print value of private variable
    def hello(self):
        print("Private Variable value: ",myClass ._ privateVar)

# Object creation and method call
foo = myClass()
foo.hello()
foo ._ privMeth