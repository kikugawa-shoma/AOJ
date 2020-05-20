V,E = map(int,input().split())
INF = 2*10**10
C = [[INF]*V for _ in range(V)]
for i in range(E):
    tmp = list(map(int,input().split()))
    C[tmp[0]][tmp[1]] = tmp[2]

for i in range(V):
    C[i][i] = 0

for k in range(V):
    for i in range(V):
        if C[i][k] == INF:
            continue
        for j in range(V):
            if C[k][j] == INF:
                continue
            C[i][j] = min(C[i][j], C[i][k] + C[k][j])

negative_cycle_f = False
for i in range(V):
    if C[i][i] < 0:
        negative_cycle_f = True

if negative_cycle_f:
    print("NEGATIVE CYCLE")
else:
    for i in range(V):
        for j in range(V):
            if C[i][j] == INF:
                print("INF",end="")
            else:
                print("{}".format(C[i][j]),end="")
            if j != V-1:
                print(" ",end="")
        print("")






