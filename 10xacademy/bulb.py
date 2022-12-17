N=int(input())
phase="OFF"
count=0
for i in range(N):
    a=input()
    if a=="Toggle" and phase=="OFF":
        phase="ON"
        count=count+1 
    elif phase=="OFF" and a=="ON":
        phase="ON"
        count=count+1      
    elif a=="OFF":
        phase="OFF"
    elif a=="ON":
        phase="ON"
    elif a=="Toggle" and phase=="ON":
        phase="OFF"
    
print(count)
