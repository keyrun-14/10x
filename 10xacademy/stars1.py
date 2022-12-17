n=int(input())
for i in range(1,n+1):
    space=n-i
    stars="*"*i
    spaces=" "*space
    print(spaces+stars)