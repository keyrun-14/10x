for i in range(int(input())):
    no_of_elements=int(input())
    arr=list(map(int,input().split()))
    for j in range(1,no_of_elements):
        key=arr[j]
        prev_index=j-1
        while prev_index>=0 and key>arr[prev_index]:
            arr[prev_index+2]=arr[prev_index]
            prev_index=prev_index-2
        arr[prev_index-2]=key
    # for j in range(1,no_of_elements):
    #     key=arr[j]
    #     prev_index=j-2
    #     while prev_index>=0 and key<arr[prev_index]:
    #         arr[prev_index+2]=arr[prev_index]
    #         prev_index=prev_index-2
    #     arr[prev_index-2]=key
    print(arr)                                      
