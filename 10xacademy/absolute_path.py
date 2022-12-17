for i in range(int(input())):
    arr=input()
    arr=arr.split("/") 
    temp=[]
    for i in range(len(arr)):
        if arr[i]=="..":
            if len(temp)==0:
                temp.append("/")
            else:
                temp.pop()
        elif arr[i]=="" or arr[i]==".":
            if arr[i]=="." and len(temp)==0:
                temp.append("/")
            continue
        else:
            temp.append("/"+arr[i])
    print("".join(temp))


# for i in range(int(input())):
#     arr=input()
#     stack=[]
#     folder=""
#     for i in arr:
#         if i=="/":
#             if folder=="..":
#                 if stack:
#                     stack.pop()
#             elif folder!="" and folder!=".":
#                 stack.append(folder)
#             folder=""
#         else:
#             folder+=i
#     output="/".join(stack)
#     print("/"+output)





# 4
# /home/
# /../
# /./
# /home/group/./../amazon/