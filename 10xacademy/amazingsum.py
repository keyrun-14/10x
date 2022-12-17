n=int(input())
add=0
for i in range(n):
    ele=int(input())
    sum=add+ele
    if ele>add:
        add=ele
    else:
        add=add
if sum>100:
    print("True")
else:
    print("False")