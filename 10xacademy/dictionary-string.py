
from collections import Counter

string=input()
words=input().split()
main_string=Counter(string)
flag=0
max_len_word=""

for i in range(len(words)):
    each_word=Counter(words[i])
    print(each_word)
    for key in each_word:
        if key not in main_string:
            flag=0
            break
        elif each_word[key]<=main_string[key]:
            flag=1
            continue
        else:
            flag=0
            break
    if flag==1 and len(max_len_word)<len(words[i]):
        max_len_word=words[i]
print(len(max_len_word))

#main string== abcdabcdpple
d1={}
# words====apple bad desk banana me this that a abc abcd pple
main string in dict:
d2={
    each word
}
d2=count
banana= a:3  but iin main string a:2

main string= abc
d1={
    a:1,
    b:1,
    c:1
}
word=cb