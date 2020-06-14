q = int(input())
S = [0]*(2*q)

for i in range(2*q):
    S[i] = input()

for i in range(q):
    X = S[2*i]
    Y = S[2*i+1]
    lx = len(X)
    ly = len(Y)
    dp = [[0]*(ly+1) for _ in range(lx+1)]
    for x in range(lx):
        for y in range(ly):
            if X[x] == Y[y]:
                dp[x+1][y+1] = dp[x][y]+1
            dp[x+1][y+1] = max(dp[x+1][y+1],dp[x][y+1],dp[x][y],dp[x+1][y])
    print(dp[lx][ly])




