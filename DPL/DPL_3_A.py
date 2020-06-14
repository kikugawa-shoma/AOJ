H,W = map(int,input().split())
M = [[0]*(W+1) for _ in range(H+1)]
for i in range(H):
    M[i+1][1:] = list(map(int,input().split()))

dp = [[0]*(W+1) for _ in range(H+1)]
for h in range(1,H+1):
    for w in range(1,W+1):
        if M[h][w] == 0:
            dp[h][w] = min(dp[h-1][w-1],dp[h-1][w],dp[h][w-1]) + 1
        else:
            dp[h][w] = 0

print(max([max(x) for x in dp])**2)

        
