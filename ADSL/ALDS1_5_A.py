n=int(input())
A=list(map(int, input().split()))
q=int(input())
m=list(map(int, input().split()))

memo=[[None]*(n+1) for _ in range(max(m)+1)]

def solver(i,m):
    if memo[m][i] != None:
        return memo[m][i]
    else:
        if m == 0:
            memo[m][i]=True
            return True
        elif i == n:
            memo[m][i]=False
            return False
        else:
            if m-A[i] >= 0:
                memo[m][i] = solver(i+1,m) or solver(i+1,m-A[i])
                return memo[m][i]
            else:
                memo[m][i] = solver(i+1,m)
                return memo[m][i]


for mi in m:
    if solver(0,mi):
        print("yes")
    else:
        print("no")
