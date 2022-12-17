# n=int(input())
# for i in range(n+1):
#     spacesup=" "*(n-i)
#     starsup=spacesup+"*"*(2*i-1)
#     print(starsup)
# for j in range(1,n):
#     spaces_down=" "*j
#     stars_down=spaces_down+"*"*(2*(n-j)-1)
#     print(stars_down)

# n = int(input())
# num = n
# res = []
# k =1
# for i in range(n):
#     res.append(" "*(num-1)+"*"*k)
#     num -=1
#     k +=2
# for i in res:
#     print(i, end="")
#     print()
# res2 = res
# res2.pop()
# print(res2)
# res2 = res2[::-1]

# for i in res2:
#     print(i, end="")
#     print()
a=[1,2,3,4,5,6,78,9]
a.pop()
print(a)
print(a[::-1])
