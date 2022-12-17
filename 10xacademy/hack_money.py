# def hack_money(a):
#     if a==1:
#         return "Yes"
#     elif a%10==0 and a%20==0:
#         return "Yes"
#     return "No"
# for i in range(int(input())):
#     a=int(input())
#     print(hack_money(a))

# def hack_money(s):
#     if a==1:
#         return "Yes"
#     elif a==0:
#         return "Yes"
#     elif a%200==0:
#         return hack_money(a-200)
#     return "NO"
    
# for i in range(int(input())):
#     a=int(input())
#     print(hack_money(a))

# def hack_money(s):
#     if a==0:
#         return "Yes"
#     elif a!=0:
#         return "No"
#     elif a%200==0:
#         return hack_money(a-200)
    
# for i in range(int(input())):
#     a=int(input())
#     print(hack_money(a))


def moneyHack(n):
    n1 = n/10
    n2 = n/20
    if n1 == 1 or n2 == 1:
        return True
    if n1 < 1 or n2 < 1:
        return False
    if moneyHack(n1) or moneyHack(n2):
        return True
t = int(input())
for i in range(t):
    n = int(input())
    if n<=0:
        print("No")
    elif n ==1:
        print('Yes')
    elif moneyHack(n):
        print("Yes")
    else:
        print('No')