# arr=[]
# for i in range(int(input())):
#     name,scholar,marks=input().split()
#     name,scholar,marks=str(name),int(scholar),int(marks)
#     arr.append([marks,scholar,name])
# print(arr)
# print()
# arr.sort(key=lambda row: (-row[0],row[1] ,row[2]))
# print(arr)
# print()
# for i in range(len(arr)-1):
#     if arr[i][0]==arr[i+1][0] and arr[i][2]<arr[i+1][2]:
#         arr[i],arr[i+1]=arr[i+1],arr[i]    
#     if arr[i][0]==arr[i+1][0] and arr[i][2]==arr[i+1][2] and arr[i][1]>arr[i+1][1]:
#         arr[i],arr[i+1]=arr[i+1],arr[i]
# print(arr)

arr=[]
for i in range(int(input())):
    name,scholar,marks=input().split()
    name,scholar,marks=str(name),int(scholar),int(marks)
    arr.append([name,scholar,marks])

arr.sort(key=lambda row: (-row[2],row[0] ,row[1]))
for i in range(len(arr)):
    print(*arr[i])
# print()
# for i in range(len(arr)-1):
#     if arr[i][0]==arr[i+1][0] and arr[i][2]<arr[i+1][2]:
#         arr[i],arr[i+1]=arr[i+1],arr[i]    
#     if arr[i][0]==arr[i+1][0] and arr[i][2]==arr[i+1][2] and arr[i][1]>arr[i+1][1]:
#         arr[i],arr[i+1]=arr[i+1],arr[i]
# print(arr)
    
# 5
# b 10 30
# a 10 30
# a 11 30
# b 11 30
# c 11 29

# 5
# b 10 30
# a 12 30
# a 11 30
# b 11 30
# c 11 29

# 5
# a 100 30
# a 20 10
# a 11 10
# a 41 20
# a 1 29

# 5
# a 100 10
# a 90 10
# a 81 30
# a 41 10
# a 1 10

# 5
# a 1 101
# b 10 10
# a 21 100
# a 41 10
# a 100 10

# 5
# a 1 10
# b 90 10
# c 81 30
# c 41 10
# d 1 10

# 5
# d 1 10
# b 90 10
# c 81 30
# c 41 10
# a 1 10

# 5
# a 91 102
# b 90 10
# a 81 102
# c 41 11
# b 1 100