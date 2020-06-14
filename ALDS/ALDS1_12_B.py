n = int(input())
C = [[] for _ in range(n)]
for _ in range(n):
    tmp = list(map(int,input().split()))
    for i in range(1,tmp[1]+1):
        C[tmp[0]].append(tuple(tmp[2*i:2*i+2]))


def dijkstra(start = 0):
    INF = 100000000
    d = [INF]*n
    visited = [False]*n

    d[start] = 0
    visited[start] = True
    S = {start}

    while 1:
        for s in S:
            for adj_weight in C[s]:
                if visited[adj_weight[0]] == False:
                    d[adj_weight[0]] = min(d[s] + adj_weight[1],d[adj_weight[0]])
        
        min_d = INF
        min_node = -1
        for i in range(n):
            if visited[i] == False and d[i] < min_d:
                min_d = d[i]
                min_node = i
        if min_node == -1:
            break
        else:
            visited[min_node] = True
            S.add(min_node)
    return d

ans = dijkstra()
for i in range(n):
    print("{} {}".format(i,ans[i]))