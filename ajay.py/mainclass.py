class Person:
    "this is docstring"
    age= 10
    display_msg = ("Ajay your age is: ",age)

    def msg(self=""):
        print("hello")

    def series(self=""):
        f = int(input("enter number: "))
        n = 1
        for n in range(1,101):
            i= f*n
            print(f,'*',n,'=',i)
obj1 =Person()

print(obj1.msg())
obj1.series()