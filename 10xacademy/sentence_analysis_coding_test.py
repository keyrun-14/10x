# from collections import Counter
# for i in range(int(input())):
#     arr=[]
#     sentence=input().split()
#     for i in range(len(sentence)):
#         arr.append(len(sentence[i]))
#     dict=Counter(arr)
#     for i in (sorted(dict)):
#         print(i,dict[i],end=" ")


for i in range(int(input())):
    dict={}
    sentence=input().split()
    for j in range(len(sentence)):
        if len(sentence[j]) in dict:
            dict[len(sentence[j])]+=1
        else:
            dict[len(sentence[j])]=1
    print(dict) 
    for i in (sorted(dict)):
        print(i,dict[i],end=" ")
