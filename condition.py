try:
   permission= input("enter permission yes or no  :  ")
   if permission == 'yes':
           print("allowed")
   elif permission=='no':
      print("denied")
   else:
         pass
except Exception as e:
    print(e)


list = ['ajay','sanjay','vijay']
name=input("enter name :")
if name in list:
    print("allowed")
else:
    print("sorry you are  not in list and your entry denied plase add your name in list below :")
    list.append("sachin")
