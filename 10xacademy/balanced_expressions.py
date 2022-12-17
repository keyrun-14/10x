string=input()
output=[]
flag=0
if string[0] in [")","}","]"]:
    flag=0
else:
    for i in string:
        if i in ["(","{","["]:
            output.append(i)
        else:
            pop_char=output.pop()
            if pop_char=="(" and  i==")":
                flag=1
            elif pop_char=="{" and  i=="}":
                flag=1
            elif pop_char=="[" and  i=="]":
                flag=1
            else:            
                flag=0
                break
if flag==1:
    print("Balanced")
else:
    print("Not Balanced")