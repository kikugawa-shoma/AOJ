n = int(input())
p = [0]*(n+1)

INF = 1000000000

for i in range(n):
    if i == 0:
        p[0],p[1] = map(int,input().split())
    else:
        tmp,p[i+1] = map(int,input().split())

dp = [[-1]*(n+2) for _ in range(n+2)]

def DFS(i,j):
    if dp[i][j] != -1:
        return dp[i][j]
    else:
        if j-i == 2:
            dp[i][j] = p[i]*p[i+1]*p[i+2]
            return dp[i][j]
        elif j-i == 1:
            dp[i][j] = 0
            return 0
        else:
            calculation_amount = INF
            for k in range(i+1,j):
                tmp = DFS(i,k) + DFS(k,j) + p[i]*p[j]*p[k] 
                calculation_amount = min(calculation_amount,tmp)
            dp[i][j] = calculation_amount
            return calculation_amount

print(DFS(0,n))