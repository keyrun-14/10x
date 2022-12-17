class person:
    def __init__(self,Name,age):
        self.Name=Name
        self.age=age
    def details(self):        
        print(self.Name)
        print(self.age)
Name,age=input().split()
Name,age=str(Name),int(age)  
person1=person(Name,age)
person1.details()

# your code goes here
# class person:
#     def __init__(self,Name,age):
#         self.Name=Name
#         self.age=age
#     def details(self):
        
#         print(self.Name)
#         print(self.age)
# Name,age=input().split()
# Name,age=str(Name),int(age)
   
# person1=person(Name,age)
# person1.details()