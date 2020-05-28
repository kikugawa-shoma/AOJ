"""
8 10
0 1
1 2
0 2
0 3
3 2
3 4
3 5
5 6
5 7
6 7
"""
import sys
sys.setrecursionlimit(100000)
V,E = map(int,input().split())
C = [[] for _ in range(V)]
for i in range(E):
    tmp = list(map(int,input().split()))
    C[tmp[0]].append(tmp[1])
    C[tmp[1]].append(tmp[0])

INF = 10000000
visited = [False]*V
visit_cnt = 1
prenum = [0]*V
parent = [-1]*V
lowest = [INF]*V

def DFS(node):
    visited[node] = True
    global visit_cnt
    prenum[node] = visit_cnt
    visit_cnt += 1
    for adj in C[node]:
        if not visited[adj]:
            parent[adj] = node
            DFS(adj)

    node_lowest = prenum[node]
    for adj in C[node]:
        if adj != parent[node] and parent[adj] != node:
            if  prenum[adj] < node_lowest:
                node_lowest = prenum[adj]
        else:
            if parent[adj] == node and lowest[adj] < node_lowest:
                node_lowest = lowest[adj]
    lowest[node] = node_lowest
        
root = 0
DFS(root)
ans = []

root_cnt = 0
for p in parent:
    if p == root:
        root_cnt += 1
if root_cnt > 1:
    ans.append(root)

for node in range(V):
    if parent[node] != root and node != root:
        if prenum[parent[node]] <= lowest[node]:
            ans.append(parent[node])
ans = set(ans)
ans = list(ans)
ans.sort()
for i in ans:
    print(i)