# s=input()
# s="cats AND*dogs-awesome"
s="a b c d-e-f%g"
spl_char=' -[@_!#$%^&*()<>?/\|}{~:]'
neww=""
for i in s:
    if i in spl_char:
        neww+="_"
    else:
        if i.isupper():
            neww+= i.lower()
        else:
            neww+=i
print(neww)
token="umt70qfhg2e"
new_token=""
for i in neww:
    if i in token:
        new_token+="--"+i+"--"
    else:
        new_token+=i
print(new_token)
