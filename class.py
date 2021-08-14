class Computer:
    def config(self):
        print("i5","1tb","8gb")
    def color(self):
        print("black")
    def brand(self):
        print("DELL")
    def print(self):
        name = str(input("enter name"))
        print("my name is ", name)
    def ifelse(self):
        a = int(input("enter number"))
        if a/2:
            print(a ,"is even number")
        else:
            print(a, "is odd number")


obj1 = Computer()
obj1.print()