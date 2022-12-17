# n=int(input())
# a=[]
# odd=0
# even=0
# for i in range(n):
#     a.append(int(input()))
# for j in range(1,n):
#     if j%2!=0:
#         odd=odd+a[j]
#     elif j%2==0:
#         even=even+a[j]
# print(a[0]+odd-even)
n = int(input())
List = []
for i in range(n):
    List.append(int(input()))
sum = List[0] + List[1]
for j in range(2,len(List)):
    if j % 2 == 0:
        sum -= List[j]
    elif j % 2 != 0:
        sum += List[j]
print(sum) 