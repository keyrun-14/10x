# string=input()
# arr=[]
# if len(string)%2 != 0:
#     print(-1)
# else:
#     count=0
#     string=list(string)
#     arr.append(string[0])
#     for i in range(1,len(string)):
#         # print(string[i])
#         if arr[len(arr)-1]==string[i]:
#             arr.append(string[i])
#         elif arr[len(arr)-1]=="{" and string[i]=="}":
#             count+=0
#         elif arr[len(arr)-1]=="}" and string[i]=="{":
#             count+=2
#         else:
#             count+=1
#             arr.pop()
#     print(count)


string=input()
arr=[]
if len(string)%2 != 0:
    print(-1)
else:
    string=list(string)
    # arr.append(string[0])
    for i in range(0,len(string)):
        if string[i]=="{":
            arr.append(string[i])
        if string[i]=="}" and len(arr)==0:
            arr.append(string[i])
        elif string[i]=="}" and arr[-1]=="{":
            arr.pop()
        elif string[i]=="}" and arr[-1]=="}":
            arr.append(string[i])
    open=0
    close=0
    for i in range(len(arr)):
        if arr[i]=="{":
            open+=1
        else:
            close+=1
    min_reverse=((open//2)+open%2) + ((close//2)+close%2)
    print(min_reverse)
# string=input()
# if len(string)%2 != 0:
#     print(-1)
# else:
#     count=0
#     string=list(string)
#     for i in range(0,len(string)-1,2):
#         # print(string[i])
#         if string[i]!=string[i+1]:
#             string[i],string[i+1]=string[i+1],string[i]
#             count+=1
#     print(count)