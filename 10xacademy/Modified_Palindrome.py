def Modified_Palindrome(string):
    
    i,j=0,len(string)-1
    count=0
    while i<len(string)//2 and j>=len(string)//2:
        if string[i]==string[j]:
            i+=1
            j-=1
        else:
            count+=1
            if count>1:
                return False
            i+=1
            j-=1
    if len(string)%2==0 and (count==1 or count==0):
        return True
    elif len(string)%2!=0 and count==1:
        return False
    else:
        return True
for i in range(int(input())):
    string=input()
    print(Modified_Palindrome(string))