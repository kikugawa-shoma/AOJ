n = int(input())
Adj = [[] for _ in range(n+1)]
C = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(tmp[1]):
        C[tmp[0]][tmp[2+j]] = 1

for i in range(n):
    print(*C[i+1][1:])