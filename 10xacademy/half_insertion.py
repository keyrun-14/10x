# arr=input()
# arr=list(arr)
# for i in range((len(arr)//2)+1,len(arr)):
#     key =arr[i]
#     previous=i-1
#     while previous>=len(arr)//2 and key<arr[previous]:
#         arr[previous+1]=arr[previous]
#         previous-=1
#     arr[previous+1]=key
# output="".join(arr)
# print(output)

def half_insertion(str):
    arr=[]
    for ele in str:
        arr.append(ele)
    for index in range((len(arr)//2)+1,len(arr)):
        key=arr[index]
        prev_index=index-1
        while prev_index>=(len(arr)//2) and key<arr[prev_index]:
            arr[prev_index+1]=arr[prev_index]
            prev_index=prev_index-1
        arr[prev_index+1]=key
    res="".join(arr)
    return res
str=input()
print(half_insertion(str))