"""
トポロジカルソート

まず入力次数が0のノードをキューに追加
その後キューから
　ノードを取り出す、
　そのノードから辺が向かう先のノードの入り次数を減らす、
　もし減らした結果入り次数が0になったらキューに追加
を繰り返す。
"""
from collections import deque
V,E = map(int,input().split())
C = [[] for _ in range(V)]
indeg = [0]*V
for _ in range(E):
    tmp = list(map(int,input().split()))
    indeg[tmp[1]] += 1
    C[tmp[0]].append(tmp[1])

q = deque()
deleted = [False]*V
ans = []
for i in range(V):
    if indeg[i] == 0:
        ans.append(i)
        q.append(i)

while q:
    node = q.pop()
    deleted[node] = True
    for adj in C[node]:
        indeg[adj] -= 1
        if indeg[adj] == 0:
            q.append(adj)
            ans.append(adj)
for node in ans:
    print(node)