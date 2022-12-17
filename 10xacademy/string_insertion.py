def stringInsertionSort(str):
    
    # Your code goes here
    str=list(str)
    str1=""
    for i in range(1,len(str)):
        key=str[i]
        previous=i-1
        while previous>=0 and key<str[previous]:
            str[previous+1]=str[previous]
            previous-=1
        str[previous+1]=key
    for i in str:
        str1=str1+i
    return str1

### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__=='__main__':
    input_string = input()
    print(stringInsertionSort(input_string))

# a="kiran"
# a[2]="K"
# print(a)
