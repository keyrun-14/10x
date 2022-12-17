def skill_level(a,b,c):

    skilllevel=[]
    for i in range(len(a)):
        if max(a)>b[i] and b[i]<min(c):
            skill=abs(max(a)-b[i])+abs(min(c)-b[i])
            skilllevel.append(skill)
        
        if max(c)>b[i] and b[i]<min(a):
            skill=abs(max(a)-b[i])+abs(min(c)-b[i])
            skilllevel.append(skill)
        
        if max(b)>c[i] and c[i]<min(a):
            skill=abs(max(b)-c[i])+abs(min(a)-c[i])
            skilllevel.append(skill)
            
        if max(a)>c[i] and c[i]<min(b):
            skill=abs(max(a)-c[i])+abs(min(b)-c[i])
            skilllevel.append(skill)
            
        if max(b)>a[i] and a[i]<min(c):
            skill=abs(max(b)-a[i])+abs(min(c)-a[i])
            skilllevel.append(skill)
            
        if max(c)>a[i] and a[i]<min(b):
            skill=abs(max(c)-a[i])+abs(min(b)-a[i])
            skilllevel.append(skill)
            
    print(min(skilllevel))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
skill_level(a,b,c)