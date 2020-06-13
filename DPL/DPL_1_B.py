N,W = map(int,input().split())
items = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*(W+1010) for _ in range(N+1)]

for i in range(N):
    for j in range(1,W+1000):
        if j - items[i][1] >= 0:
            dp[i+1][j] = max(dp[i][j], dp[i][j-items[i][1]]+items[i][0])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[N][W])
