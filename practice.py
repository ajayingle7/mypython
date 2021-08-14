x= 23
class Myclass:
    "this is my class"
    name = str(input("enter full name: "))
    print("my name is ", name)


    def myfun(self,salary,city):
        self.salary = salary
        self.city = city
        print("my city is ", city, "my salary is ", salary)
        martial_status = "status = single"
        print(martial_status)

    def myfun2(self):
        a = int(input("enter number:  "))
        if a/2:
            print( a," is even number")
        elif a!=2:
            print("this is odd number")

obj1 =Myclass()
obj1.myfun(city="pune",salary=23456)
obj1.myfun2()
