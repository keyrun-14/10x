# n=int(input())
# a=[]

# for i in range(n):
#         ele=int(input())
#         a.append(ele)

# for i in range(n-1):
#         if a[i]>=a[i+1]:
#            a[i+1]=a[i]
# for i in range(n):
#     print(a[i])



n=int(input())

first_element=int(input())

print(first_element)

for i in range(n-1):
        ele=int(input())
        if ele > first_element:
                first_element
                print(ele)
        else:
                print(first_element)


