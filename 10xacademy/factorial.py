# n=int(input())
# for j in range(n):
#     fact=1
#     for i in range(1,j+1):
#         fact=fact*i
#         # if fact%365==0:
#         #     print(j)
#     # if n==0:
#     #     print(1)
#     # elif n<0:
#     #     print("undefined")
#     # else:
#     #     print(fact)
#     print(fact,"jhkhgdkt")
#     fact=fact%365
#     print(fact,"mod",j)

# n=int(input())
# for j in range(n):
#     fact=1
#     for i in range(1,j+1):
#         fact=fact*i
#     print(fact,"jhkhgdkt")
#     fact=fact%365
#     print(fact,"mod",j)
   
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
 
    def language(self):
        print("Hindi is the most widely spoken language of India.")
 
    def type(self):
        print("India is a developing country.")
 
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")
 
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()