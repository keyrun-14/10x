s=input()
t=input()
if len(s)==len(t):
    d1={}
    for i in s:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    d2={}
    for i in t:
        if i in d2:
            d2[i]+=1
        else:
            d2[i]=1
    print(d1)
    print(d2)    
    if len(d1)==len(d2):
        if list(d1.values())==list(d2.values()):
            l1 = list(d1.keys())
            l2 = list(d2.keys())
            d3 = {}
            for i in range(len(l1)):
                d3[l1[i]] = l2[i]
            print(d3)
            dummy_string = ""
            for i in s:
                dummy_string += d3[i]
            print(dummy_string)
            if dummy_string == t:
                print(True)
            else:
                print(False)
else:
    print(False)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2288
# }
# print(thisdict.keys())
# paperss
# kbsstzz
# print([1,2,3,4]==[1,2,3,4])
