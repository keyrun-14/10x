def insertionSort(A,n):
    for i in range(1,n):
        current=A[i]
        previous=i-1
        while previous>=0 and current<A[previous]:
            A[previous+1]=A[previous]
            previous-=1
        A[previous+1]=current
    return A
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*insertionSort(arr, n))