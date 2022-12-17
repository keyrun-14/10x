def record(n,score):
    count1=0
    count2=0
    mam,mim=score[0],score[0]
    for i in range(n):
        # maxm=max(score[:i+1])
        # mimm=min(score[:i+1])
        # print(score[i]," ",maxm," ",mimm)
        if mam>=score[i]:
            mam=mam
        else:
            mam=score[i]
            count1=count1+1
        if mim<=score[i]:
            mim=mim
        else:
            mim=score[i]
            count2=count2+1
    print(count1,count2)
n=int(input())
score=list(map(int,input().split()))[:n]
record(n,score)
