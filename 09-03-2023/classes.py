#classes
class Myclass:
    x=5
#above we have created class now we are going to create object for that class.
p1=Myclass()
print(p1.x)

##__init__()function--to assign value to object properties.

class Employee:
    def __init__(self,name,id):
        print('init is invoked')
        self.name=name
        self.id=id
e1=Employee('Sugu',1234)
e2=Employee('Thiru',7452)
print(e1.name)

##__str__() function--When the class's object is represented as string
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'{self.name} and age is {self.age}' 
s1=Student('Sugu',21)
print(s1.name)
print(s1.age)
print(s1)#here s1 is represented as string.

#Object methods
class Demo:
    def __init__(self,name,location):
        self.name=name
        self.location=location
    def printdetails(self):
        print('Hello,I am '+self.name +' and my native is ' +self.location)
per1=Demo('Sugu','Elandhai')
print(per1.name)
per1.printdetails()

#self parameter --It is used to refer the current instance of the class and is used to access variables t
#that belongs to the class.
#And it doesnt have to be named as self and it can be named as anything by our choice but it should be the first parameter in any function in the class..

class BPM:
    def __init__(finger,name,addr):
        finger.name=name
        finger.addr=addr
    def biometric(finger):
         print(finger.name+"'s fingerprint is not working.You should go to "+finger.addr+" office")
per2=BPM('Suve','Thirumanur')
#over writing object properties
per2.addr='Elandai'
per2.biometric()
#we can deleted object properties.
del per2.addr
# per2.biometric()
per3=BPM('Thiru','Chennai')
per3.biometric()
#we can delete the object itself\
del per3
# print(per3.name)#it says error that it is not defined.

#METHOD May call other method using self.
class defi:
    def __init__(self,x):
        self.x=x
        
    def add(self):
        
        return self.x**2
    def cube(self):
        return self.x**3

n=defi(8)
print(n.add())
print(n.cube())
# print(n.addtwice())



