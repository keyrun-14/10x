# # # a=[1,2,3,4,5,6]
# # # for i in range(1,7):
# # #     print(a[i])
# # n=int(input())
# # a=list(map(int,input().split()))[:n]
# # print(a)
# # List = [int(i) for i in input().split()][:n]
# # list1=[6,23,3,2,0,9,8,75]
# # print(list1[1::2])
# # print(list1.index(100))
# # for i in range(7,-2,-9):
# #     for j in range(i):
# #         print(j,end=" ")
# # for i in range(1,5):
# #     print("*",end=" ")
# #     i=i+2
# # print(4+3%5)
# # a=[[1,2,3],[4,5,6],[7,8,9]]
# # print(a[1][2])
# # a=[1,2,3,4]
# # b=[1,2,3]
# # c=[1,2,3]
# # a.append(b)
# # a.append(c)
# # s="hello world"
# # arr=s.split(" ")
# # print(arr)
# # arr=[1,2,3,4]
# # for i in range(1,4):
# #     arr
# # for i in range(6):
# #     if i==5:
# #         break
# #     else:
# #         print(i)
# # else:
# #     print("here")
# # N=int(input())
# # for i in range(1,10**9):
# #     if i%2==0 and i%N==0:
# #         print(i)
# #         break
# # n=10
# # while n>0:
# #     print(n)
# #     n=n-1
# # a=[12, 31, 10, 14, 21, 11, 2, 23, 17]
# # a.sort()
# # print(a)
# # avg=((a[((len(a)//2)-1)]+a[(len(a)//2)]))/2
# # print(avg)
# # print(11|12)
# # print(5&21)
# # a,b=map(int,input().split())
# # print(a)
# # a=set('TAMVADA')
# # print(a)
# # for i in range(20,-2,-1):
# #     print(i)
# # a="kiran"
# # a=list(a)
# # print(a)
# # my_tuple = ('sara', 6, 5, 0.97)
# # my_list = ['sara', 6, 5, 0.97]

# # print(my_tuple[0:3])     # output => 'sara'
# # print(my_list[0])     # output => 'sara'
# # my_tuple[0] = 'ansh'    # modifying tuple => throws an error
# # my_list[0] = 'ansh'    # modifying list => list modified
# # print(my_tuple[0])     # output => 'sara'
# # print(my_list[0])     # output => 'ansh'

# # # Common functions used with the built-in set() function:
# # set_1 = set([1, 2, 3, 4, 5])
# # set_2 = set([4, 5, 6, 7, 8])

# # print(set.intersection(set_1, set_2)) # Calculates the intersection of 2 sets
# # print(set.union(set_2, set_1)) # Calculates the union of 2 sets
# # print(set.difference(set_2, set_1)) # Looks for the difference between 2 lists
# # #set.add(set_name, number_to_add) # Adds a new member to the set
# # print(set.copy(set_1)) # Outputs the set given in the brackets
# # #set.discard(set_2, number_to_remove) # Removes an element in the set


# # Python program to demonstrate differences
# # between normal and frozen set
 
# # Same as {"a", "b","c"}
# # normal_set = set(["a", "b","c"])
 
# # print("Normal Set")
# # print(normal_set)
 
# # # A frozen set
# # frozen_set = frozenset(["e", "f", "g"])
 
# # print("\nFrozen Set")
# # print(frozen_set)
 
# # Uncommenting below line would cause error as
# # we are trying to add element to a frozen set
# # frozen_set.add("h")

# # def rearrange(arr, n):
# #     temp = []
# #     small, large = 0, n-1
# #     for i in range((n//2)+1):
# #         if small!=large:
# #             temp.append(arr[large])
# #             large -= 1
# #             temp.append(arr[small])
# #             small += 1
# #         else:
# #             temp.append(arr[n//2])
# #     print(temp)
# # arr = [1, 2, 3, 4, 5]
# # n = len(arr)
# # print("Original Array")
# # print(arr)
# # print("Modified Array")
# # print(rearrange(arr, n))

# # def rearrange(arr, n):
# #     temp = []
# #     small, large = 0, n-1
# #     for i in range((n//2)):
# #         temp.append(arr[large])
# #         large -= 1
# #         temp.append(arr[small])
# #         small += 1
# #     if n%2!=0:
# #         temp.append(arr[n//2])
# #     return temp
# # arr = [1, 2, 3, 4, 5,6]
# # n = len(arr)
# # print("Original Array")
# # print(arr)
# # print("Modified Array")
# # print(rearrange(arr, n))

# # a="k.i.r.a.n"
# # b=list(a)
# # print(b)
# # for i in range(len(a)-1,-1,-1):
# #     print(a[i])

# # v="kiran","kumar","tavada"
# # print(v)

# # a=[4,3,2,1]
# # a.sort()
# # count=0
# # for i in range(len(a)-1,0,-1):
# #     print(a[i],"aaaaaaaaaa")
# #     for j in range((len(a)-1)-i+1,-1,-1):
# #         print(a[j],"bbb")
# #         if a[i]%a[j]==0:
# #             count=count+1
# #             break
# # print(count)

# # s=["c","a","z","z","b","b","b"]
# # d={}
# # for i in s:
# #     if i in d:
# #         d[i]+=1
# #     else:
# #         d[i]=1

# # # print(dict(sorted(d.items(), key=lambda item: (item[1],item[0]))))
# # a=0
# # for i in range(10):
# #     if i==2:
# #         pass
# #     else:
# #         a=i
# # print(a)
# e=list(enumerate("python"))
# a=list(range(len("python")))
# print(e,a)
# a=["1","3","-9","0"]
# y=sorted(a)
# print(y)

# def rec(arr,i,m):
#     if i<0:
#         return 1
#     return arr[m] + rec(arr,i-1,m-i)
# arr=[1,2,3,4,5]
# m=2
# i=len(arr)-1
# rec(arr,i,m)
a=123456/1000
print(a)