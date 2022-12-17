
# def norml(initial):
#     if len(initial)>=2:
#         [final.append(initial[i]) if initial[i]*2>=initial[i+1] else final.append(initial[i+1]) for i in range(len(initial)-1)]
#         return final
#     else:
#         return ("at least 2 elements to be given")
# initial=list(map(int,input().split()))
# final=[]
# print(norml(initial))

# def listing(arr,n):
#     arr.sort()
#     print(arr)
#     final=[]
#     each=[]
#     for i in range(len(arr)-1):
#         str_len = len(str(arr[i]))
#         final_len=str_len-n
#         if final_len <0:
#             return (f"num should be min length {n}")
#         else:        
#             if arr[i]//(10**final_len)==arr[i+1]//(10**final_len):
#                 each.append(arr[i])
#             else:
#                 each.append(arr[i])
#                 final.append(each)
#                 each=[]
#     if len(each)>0:
#         final.append(each)
#         if arr[-1]//(10**final_len)==final[-1][-1]//(10**final_len):
#             final[-1].append(arr[-1])
#         else:
#             final.append([arr[-1]])
#     else:
#         final.append([arr[-1]])
#     return (final)
# arr=list(map(int,input().split()))
# n=int(input())
# print(listing(arr,n))

def nested_to_flatten(arr):    
    for element in arr:
        # print(element,end=" , ")
        if type(element)==list:

            # print(element,end=" , ")
            nested_to_flatten(element)
        else:
            # print(final)
            # print(element)
            final.append(element)
    return(final)
# arr=[1,[2],[[3,4]],[[[[5]]]],7]
arr=[1,2,3,4,[[[[[[[[[[[[[[[[[[[[6,7,8,9,10]]]]]]]]]]]]]]]]]]]],12345]
final=[]
print(nested_to_flatten(arr))

