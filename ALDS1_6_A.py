n=int(input())
A=list(map(int,input().split()))

def counting_sort(A):
    n=len(A)
    K=max(A)
    C=[0]*(K+1)
    for i in range(n):
        C[A[i]]+=1
    
    for i in range(1,K+1):
        C[i]=C[i-1]+C[i]

    ans=[0]*n

    for j in range(n-1,-1,-1):
        ans[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return ans

print(*counting_sort(A))