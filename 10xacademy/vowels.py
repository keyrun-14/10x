string=input()
vowels={'a':0,'e':1,'i':2,'o':3,'u':4}
for i in string:
    if  i in vowels:
        print(i,end=" ")