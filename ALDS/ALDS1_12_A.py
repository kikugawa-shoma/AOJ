import heapq

n = int(input())
M = [list(map(int,input().split())) for _ in range(n)]

q = []

visited = [False]*n

adjs = []
sum_cost = 0
node = 0
visited[node] = True
cnt = 1

while 1:
    for i in range(n):
        if M[node][i] != -1 and visited[i] == False:
            heapq.heappush(q, (M[node][i], i))
    while 1:
        mincost,node = heapq.heappop(q)
        if visited[node] == False:
            break
    sum_cost += mincost
    visited[node] = True
    cnt += 1
    if cnt == n:
        break

print(sum_cost)


    
    
