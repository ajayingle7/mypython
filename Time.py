class myclass:

    def myfun(self,i=10):
        for i in range(100):
            print(i)


    def myfun2(self,num=10):
          for j in range(num):
              for k in range(num):
                print("*", end=" ")
              print()

    def myfun3(self,a=int(input("enter numberr"))):
        self.a = a
        if (a>0):
            print(a, "is positive number")
        elif (a==0):
            print(a, "is zero")
        elif (a<0):
            print(a, "is negetive number")
        else:
            pass



obj1 = myclass()
obj1.myfun()
