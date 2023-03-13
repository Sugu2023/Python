class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname+self.lname)
person1=Person('Thiru','Murugan')
person1.printname()
class Student(Person):#Inheritance with methods their own methods
  def __init__(self,finame,liname):
       self.fname=finame
       self.lname=liname
  def printdetails(self):
         print(self.fname,self.lname)
      
x=Student('Sugu','maran')
print(x.fname)
x.printdetails()
#------------------------------------------------------------------------
#calling their parents properties to use for them
class Demo:
    def __init__(self,name1,location,sal):
        self.name1=name1
        self.location=location
        self.sal=sal
    def parentprinter(self):
        print('Hi i am',self.name1,'.My navtive is',self.location,'. My salary is',self.sal)
class demo(Demo):
    def __init__(self, name1, location, sal,rel):
        super().__init__(name1,location,sal)
        self.rel='son'
    def childprinter(self):
                print('Hi i am',self.name1,'.My navtive is',self.location,'. My salary is',self.sal,'i am Demo',self.rel)

# D1=Demo('Ram','elandai',50000)
# D1.parentprinter()
d1=demo('Sugu','Trichy',40000,'son')
d1.childprinter()
# d2=demo()
# d2.childprinter()

#usinng parent name
class Employee:
     def __init__(self,ename,eid):
          self.ename=ename
          self.eid=eid
     def empdetails(self):
          print('Employee name:',self.ename,'EMP-ID:',self.eid)
class worker(Employee):
     def __init__(self, ename, eid):
          Employee.__init__(self,ename, eid)
x=worker('Vasanth',1243)
x.empdetails()
