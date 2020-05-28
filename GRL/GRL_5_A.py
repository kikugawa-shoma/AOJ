from collections import deque

n = int(input())
C = [[] for _ in range(n)]
for _ in range(n-1):
    s,t,w = map(int,input().split())
    C[s].append((t,w))
    C[t].append((s,w))

INF = 10000000000

def BFS(start):
    D = [INF]*n
    q = deque()
    visited = [False]*n
    q.append(start)
    visited[start] = True
    D[start] = 0
    while q:
        node = q.pop()
        visited[node] = True
        for adj,w in C[node]:
            if D[node] + w < D[adj]:
                D[adj] = D[node] + w
            if not visited[adj]:
                q.append(adj)
    return D

D = BFS(0)
max_ind1 = D.index(max(D))
D = BFS(max_ind1)
print(max(D))

        


