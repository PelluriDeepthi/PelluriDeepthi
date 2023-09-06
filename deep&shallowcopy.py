class myClass:
    myName = "Mohan"
    myAge = 30
    myLocation = "Hyderabad"

    def __init__(self):
        print("The class details are","\n", self.myName, "\n" ,self.myAge, "\n", self.myLocation)

myObj = myClass()

#updating myname and myage
myObj.myName = "Ranga"
myObj.myAge = 45
print("The name of the person is:", myObj.myName)
print("The age of the person is:", myObj.myAge)
Obj1 = myObj

print("The memory location of my object is:", id(myObj))
