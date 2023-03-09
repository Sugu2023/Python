class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname+self.lname)
person1=Person('Thiru','Murugan')
person1.printname()
class Student(Person):#Inheritance
  def __init__(self,fname,lname):
      Person.__init__(fname,lname)
      
      def printname(self):
       print(self.fname,self.lname)
      
x=Student('Sugu','maran')
x.printname1()
#------------------------------------------------------------------------
