from calendar import c


def word_smith(): 
    alphabets=list(map(str,input().split()))  
    return  delete_alpha(alphabets)
def delete_alpha(alphabets):
    string=input()
    for i in string:
        string=string.replace(i,"")
    return string  
print(word_smith())

# a b c
# abzzzzzzzzzzzzeeeeeee
# 1-> bzzzzzzzzzzzzeeeeeee
# 2-> zzzzzzzzzzzzeeeeeee
# 3->zzzzzzzzzzzzeeeeeee
# output=zzzzzzzzzzzzeeeeeee


# def word_smith(): 
#     alphabets=list(map(str,input().split()))     
#     return  delete_alpha(alphabets)
# def delete_alpha(alphabets):
#     string=input()  
#     k=string  
#     for i in alphabets:
#         for j in range(len(string)):
#             if i==string[j]:
#                 k=k.replace(string[j],"")
#     return k  
# print(word_smith())





# alphabets=list(map(str,input().split()))
# string=input()
# k=string
# for i in alphabets:
#     for j in range(len(string)):
#         if i==string[j]:
#             k=k.replace(string[j],"")
# print(k)


