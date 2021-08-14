
#program of simple interest calculation

principle_value = int(input("enter principle value: "))
rate = int(input("enter rate:  "))
time = int(input("enter time:  "))
simple_interest =int( principle_value*rate*time/100)
print(simple_interest)
