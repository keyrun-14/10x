n=int(input())
string=input()
lower=[]
upper=[]
for i in range(n):
    if string[i].islower():
        lower.append(string[i])
    else:
        upper.append(string[i])
lower.sort(reverse=True)
upper.sort(reverse=True)
output=[]
for i in range(n):
    if string[i].islower():
        output.append(lower[len(lower)-1])
        lower.pop()
    else:
        output.append(upper[len(upper)-1])
        upper.pop()
final_word=""
for i in range(n):
    final_word+=output[i]
print(final_word)