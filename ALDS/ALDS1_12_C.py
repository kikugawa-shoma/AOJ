import heapq

n = int(input())
C = [[] for _ in range(n)]
for _ in range(n):
    tmp = list(map(int,input().split()))
    for i in range(1,tmp[1]+1):
        C[tmp[0]].append(tuple(tmp[2*i:2*i+2]))

q = []

def heap_dijkstra(start = 0):
    visited = [False]*n
    INF = 10000000000
    d = [INF]*n

    d[start] = 0
    visited[start] = True
    add_node = start

    for i in range(n-1):
        for adj_weight in C[add_node]:
            if visited[adj_weight[0]] == False:
                heapq.heappush(q,(d[add_node]+adj_weight[1],adj_weight[0]))

        while 1:
            tmp = heapq.heappop(q)
            if visited[tmp[1]] == False:
                min_weight = tmp[0]
                min_node = tmp[1]
                break
        
        add_node = min_node
        visited[min_node] = True
        d[min_node] = min_weight
    
    return d

D = heap_dijkstra()

for i in range(n):
    print("{} {}".format(i,D[i]))