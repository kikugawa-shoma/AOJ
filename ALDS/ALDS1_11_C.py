from collections import deque

n = int(input())
C = [[] for _ in range(n+1)]
for _ in range(n):
    stdin = list(map(int,input().split()))
    for j in range(stdin[1]):
        C[stdin[0]].append(stdin[2+j])

q = deque()
q.append(1)
d = [-1]*(n+1)
visited = [False]*(n+1)
d[1] = 0
visited[1] = True

while q:
    node = q.popleft()
    for adj in C[node]:
        if visited[adj] == False:
            q.append(adj)
            d[adj] = d[node]+1
            visited[adj] = True

for i in range(1,n+1):
    print("{} {}".format(i,d[i]))









