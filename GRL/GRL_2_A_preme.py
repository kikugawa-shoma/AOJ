import heapq

V,E = map(int,input().split())
C = [[] for _ in range(V)]
for _ in range(E):
    s,t,w = map(int,input().split())
    C[s].append([t,w])
    C[t].append([s,w])

visited = [False]*V
visited[0] = True
q = []
node = 0
node_cnt = 1
ans = 0

while node_cnt < V:
    for adj,w in C[node]:
        if not visited[adj]:
            heapq.heappush(q,(w,adj))
    while 1:
        weight,node = heapq.heappop(q)
        if not visited[node]:
            break
    visited[node] = True
    ans += weight
    node_cnt += 1
print(ans)


    


