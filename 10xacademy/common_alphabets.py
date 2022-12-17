n = int(input())
d = {}
first = input()
for letter in first:
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1
for i in range(1,n):
    s = input()
    for k in d:
        d[k] = min(d[k], s.count(k))
let = []
for key in d:
    if d[key] > 0:
        let.append(key)
let.sort()
for i in let:
    print(i + ' ' + str(d[i]))



Input -- gmefgek mgfgk kinfgggg

Explanation --
g 2
f 1
k 1

output -- 
f 1
g 2
k 1
Solution --

gmefgek
d = {}

g = 2
m = 1
e = 2
f = 1
k = 1

for k in d:
    d[k] = min(d[k], s.count(k))

s = mgfgkgl
s.count(g) = 3 --> min(2, 3) = 2
g = 2
s.count(m) = 1 --> min(1,1) = 1
m = 1
s.count(e) = 0 --> min(1,0) = 0
e = 0
f = 1
k = 1
#updated dictionary
g=2
m=1
e=0
f=1
k=1

s = kinfgggg
s.count(g) = 4 --> min(2,4) = 2
g=2
m=0
e=0
f=1
k=1
Abhishek Ranjan2:35 PM
res = []
if(dict[key]>0)
	res.append(key)
res = [g f k]

res.sort --> [f g k]

for ch in res
print(ch + ' ' dict[ch]) --> f 1
			     g 2
			     k 1