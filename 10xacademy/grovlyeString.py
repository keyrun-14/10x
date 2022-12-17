# for i in range(int(input())):
#     string=input()
#     string_in_list=[]
#     string_in_list[:0]=string
#     string_in_list.sort()
#     mid=len(string_in_list)//2
#     string_in_list=string_in_list[:mid]+string_in_list[-1:mid-1:-1]
#     print(string_in_list[:mid],"    " ,string_in_list[len(string)-1:mid-1:-1])
#     print(string_in_list)
#     print("".join(string_in_list))
#     sum=0
#     for i in range(len(string)//2):
#         sum=sum+( (mid-i)*(ord(string_in_list[i])) + (mid-i)*(ord(string_in_list[(len(string)-1)-i]))   )
#         print(sum)




for i in range(int(input())):
    string=input()
    arr=[]
    right=[]
    if string.isalpha() and string.islower() and len(string)%2!=0:
        string_in_list=[]
        string_in_list[:0]=string
        string_in_list.sort()
        mid=len(string_in_list)//2        
        for i in range(0,len(string),2):
            arr.append(string_in_list[i])
        for i in range(1,len(string),2):
            right.append(string_in_list[i])    
        right=right[::-1]
        arr=arr+right
    print("".join(arr))



# input=abcdefghi
# a c e g i h f d b

# len=9
# mid=e  9//2=4
#  calc= ascii(a)=97 dist from mid is 4   4-0=4 4*97 
#  calc =ascii(b)=98 dist from mid is 3   4-1=3 3*98
#  ...
#  97*4 98*3 99*2 100*1 101*0 102*1 103*2 104*3 105*4

#   97*4 99*3 101*2 103*1 105*0 104*1 102*2 100*3 98*4




for _ in range(int(input())):
    s=input()
    ss=[i for i in s]
    ss.sort()
    s="".join(ss)
    k=len(s)-1
    i=(len(s)-1)//2
    j=(len(s)-1)//2
    ss[i]=s[k]
    k-=1
    i-=1
    j+=1
    while i>=0 and j<len(s):
        ss[j]=s[k]
        k-=1
        j+=1
        ss[i]=s[k]
        k-=1
        i-=1
    print("".join(ss))
#     abcgefghi


#              e h g
# i=3
# j=6
# k=6
