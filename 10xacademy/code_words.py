No_of_testCases=int(input())
for i in range(No_of_testCases):
    morseCode=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    words=list(map(str,input().split()))
    final=set()
    for i in words:
        res=""
        for j in i:
            res=res+morseCode[ord(j)-ord("a")]
        final.add(res)
    print(len(final))