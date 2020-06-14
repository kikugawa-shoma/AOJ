"""
TLE
"""

n = int(input())
A = [-1]*(n+1)
A[1:] = [int(input()) for _ in range(n)]


def LIS1(A):
    L = [0]*(n+1)
    #P = [-1]*(n+1)

    for i in range(1,n+1):
        k = 0
        for j in range(1,i):
            if A[i] > A[j] and L[j] > L[k]:
                k = j
        L[i] = L[k] + 1
    #    P[i] = k
    return L#,P

L = LIS1(A)

print(max(L))


