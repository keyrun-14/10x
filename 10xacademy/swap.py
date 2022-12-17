# def swap(a,b):
#     c=0
#     c=a
#     a=b
#     b=c
#     print(a)
#     print(b)
# a=int(input())
# b=int(input())
# swap(a,b)

def swap(a,b):
    a,b=b,a
    return a,b
a=int(input())
b=int(input())
a,b=swap(a,b)
print(a)
print(b)
swap(a,b)


