N=int(input())
A=list(map(int,input().split()))

def selectionSort(A,N):
    num=0
    for i in range(N-1):
        minj=i
        for j in range(i,N):
            if A[minj] > A[j]:
                minj=j
        if minj != i:
            tmp=A[i]
            A[i]=A[minj]
            A[minj]=tmp
            num += 1
    return A,num

A,N=selectionSort(A,N)
print(*A)
print(N)
