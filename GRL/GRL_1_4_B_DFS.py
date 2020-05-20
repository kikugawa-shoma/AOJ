from collections import deque
ans = deque()
V,E = map(int,input().split())
C = [[] for _ in range(V)]
for _ in range(E):
    tmp = list(map(int,input().split()))
    C[tmp[0]].append(tmp[1])

visited = [False]*V


def DFS(node):
    visited[node] = True
    for adj in C[node]:
        if not visited[adj]:
            DFS(adj)
    ans.appendleft(node)


for i in range(V):
    if not visited[i]:
        DFS(i)


for node in ans:
    print(node)