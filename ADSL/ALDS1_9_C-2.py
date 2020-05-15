import heapq
heap = []
while 1:
    order = input().split()
    if order[0] == "insert":
        k = -int(order[1])
        heapq.heappush(heap,k)
    elif order[0] == "extract":
        print(-heapq.heappop(heap))
    elif order[0] == "end":
        break
        
