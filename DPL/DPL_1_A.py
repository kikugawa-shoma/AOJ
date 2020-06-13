n,m = map(int,input().split())
C = list(map(int,input().split()))
INF = 50010
dp = [[INF]*(n+1) for _ in range(m+1)]


for i in range(m):
    dp[i+1][0] = 0
    for j in range(1,n+1):
        if j-C[i] >= 0:
            dp[i+1][j] = min(dp[i+1][j-C[i]]+1,dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[m][n])

