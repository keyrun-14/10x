def Balanced_Parentheses(res,n,i,num_open,num_close,curr):
    if num_close==n and num_open==n:
        res.append(curr)
        return
    if num_open<n:
        Balanced_Parentheses(res,n, i+1, num_open+1, num_close, curr+ '(')
    if num_close<num_open:
        Balanced_Parentheses(res,n, i+1, num_open, num_close+1, curr+ ')')
def getAllValidCombinations(n):
    res=[]
    Balanced_Parentheses(res,n,0,0,0,'')
    return res
n=int(input())
AllValidCombinations=getAllValidCombinations(n)
AllValidCombinations.sort()
for expr in AllValidCombinations:
    print(expr)