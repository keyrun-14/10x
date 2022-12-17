# def scoring_exam(arrTi):
#     if len(arrTi)>1:
#         mid=len(arrTi)//2
#         left=arrTi[:mid]
#         right=arrTi[mid:]
#         scoring_exam(left)
#         scoring_exam(right)
#         i,j,k=0,0,0
#         while i<len(left) and j<len(right):
#             if left[i]>right[j]:
#                 arrTi[k]=left[i]
#                 i+=1
#             else:
#                 arrTi[k]=right[j]
#                 j+=1
#             k+=1
#         while i<len(left):
#             arrTi[k]=left[i]
#             i+=1
#             k+=1
#         while j<len(right):
#             arrTi[k]=right[j]
#             j+=1
#             k+=1
#     return arrTi   
# N,Q=map(int,input().split())
# arrTi=list(map(int,input().split()))
# arrSi=list(map(int,input().split()))
# (scoring_exam(arrTi))
# final=[]
# sum1=0
# for x in arrTi:
#     sum1=sum1+x
#     final.append(sum1)
# for i in range(Q):
#     query=int(input())
#     print(final[query-1])
        


N,Q=map(int,input().split())
arrTi=list(map(int,input().split()))
arrSi=list(map(int,input().split()))
arrTi.sort(reverse=True)
final=[]
sum1=0
for x in arrTi:
    sum1=sum1+x
    final.append(sum1)
for i in range(Q):
    query=int(input())
    print(final[query-1])