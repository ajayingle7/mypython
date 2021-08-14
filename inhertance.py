class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname = lname
    def printname(self):
        print("your fname is:",self.fname, "your lname is ",self.lname)

obj= Person(fname=input("enter fname"),lname=input("enter lname"))
obj.printname()

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year
    def welcome(self):
        print("welcome",self.fname,self.lname,"to the class of",self.graduationyear)
obj=Student("Ajay","Ingle",2021)
obj.welcome()


f = open("inheritanceBASIC.py",'w')