def difference_sum_even_odd_index(list):
    even=0
    odd=0
    for i in range(0,len(list),2):
        even=even+list[i]

    for i in range(1,len(list),2):
        odd=odd+list[i]
 
    print(even-odd)
n=list(map(int,input().split()))
difference_sum_even_odd_index(n)
