N=int(input())
A=list(map(int,input().split()))


def bubbleSort(A,N):
    flag=1
    num=0
    i=0
    while flag:
        flag=0
        j=0
        for i in range(N-j-1):
            if A[i] > A[i+1]:
                tmp=A[i]
                A[i]=A[i+1]
                A[i+1]=tmp
                flag=1
                num += 1
        j += 1
    return A,num

(A,N)=bubbleSort(A,N)
print(*A)
print(N)

