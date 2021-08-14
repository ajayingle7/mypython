#this is module creating program
class myclass:
    def myfun(self,a,b):
        self.a = a
        self.b = b
        print(a+b)

    def myfun2(self,name, city):
        print("my name is ", name, "and i am from " , city)


obj1 = myclass()
obj1.myfun(11,11)
obj1.myfun2("ajay","pune")