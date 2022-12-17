string_1=input()
string_2=input()
flag=0
for i in string_2:
    if i in string_1:
        flag=1
    else:
        flage=0
        break
if flag==1:
    print(1)
else:
    print(0)

# from collections import Counter
# string_1=input()
# string_2=input()
# str1=Counter(string_1)
# str2=Counter(string_2)
# if str1==str2:
#     print(1)
# else:
#     print(0)