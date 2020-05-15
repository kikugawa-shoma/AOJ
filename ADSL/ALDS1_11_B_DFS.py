n = int(input())
C = [[] for _ in range(n+1)]

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(tmp[1]):
        C[tmp[0]].append(tmp[2+j])

visited = [False]*(n+1)
d = [0]*(n+1)
f = [0]*(n+1)
t = 0

def DFS(node):
    visited[node] = True
    global t
    t += 1
    d[node] = t
    for adj in C[node]:
        if visited[adj] == False:
            DFS(adj)
    t += 1
    f[node] = t

for i in range(1,n+1):
    if visited[i] == False:
        DFS(i)

for i in range(1,n+1):
    print("{} {} {}".format(i,d[i],f[i]))
        



