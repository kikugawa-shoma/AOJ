N=int(input())
A=list(map(int,input().split()))

for i in range(N):
    j=i-1
    insertion_A=A[i]
    while j >= 0:
        if A[j] > insertion_A: 
            A[j+1] = A[j] 
        else:
            break
        j -= 1
    A[j+1]=insertion_A
    print(*A)
