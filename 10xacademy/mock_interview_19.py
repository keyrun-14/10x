# # "Given an array put all negative elements at the left side, positive elements at the right side. 
# # While doing so, preserve the order of elements. Without adding any extra arrays - space complexity For eg: [-2, -4, 9,-1, 6, 98,0,-54,53,2]
# # Output : [-2,-4,-1-54,0,9,6,98,53,2]"

# arr  =    [-2, -4, 9,-1,6 , 98,0,-54,53,2]
# #Output : [-2,-4,-1-54,0,9,6,98,53,2]
# n=len(arr)

# for i in range(n-1):
#     if arr[i]>0:
#         arr[i],arr[i+1]=arr[i+1],arr[i]
#     print(arr)





from typing import Counter
pattern="abba"
pattern=list(pattern)
s="dog cat cat dog"
s=s.split(" ")
d1=Counter(pattern)
print(d1)
d2=Counter(s)
print(d2)
if len(d1)!=len(d2):
    print("false")
else:

    flag=0
    for key in d1:
        if d1[key]==d2[key]:
            print(d1[key],"    ",d2[key])
            flag=1
        else:
            flag=0
            break
    # for i in range(len(pattern)):
    #     if s[i][0]==pattern[i]:
    #         flag=1
    #     else:
    #         flag=0
    #         break
    if flag==1:
        print("true")
    else:
        print("false")
        