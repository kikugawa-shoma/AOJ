from collections import deque

H,W = map(int,input().split())
W += 1
M = [[0]*(W+1) for _ in range(H+1)]
for i in range(H):
    M[i+1][1:] = list(map(int,input().split())) + [1]

h_table = [[0]*(W+1) for _ in range(H+1)]
for h in range(1,H+1):
    for w in range(1,W+1):
        if M[h][w] == 0:
            h_table[h][w] = h_table[h-1][w] +1
        else:
            h_table[h][w] = 0

max_S = 0
for h in range(1,H+1):
    stuck = deque()
    hist = h_table[h][:]
    for w in range(1,W+1):
        if stuck == deque() or stuck[-1][0] < hist[w]:
            stuck.append([hist[w],w])
        elif stuck[-1][0] > hist[w]:
            while 1:
                rect = stuck.pop()
                max_S = max(max_S,rect[0]*(w-rect[1]))
                if stuck == deque() or stuck[-1][0] <= hist[w]:
                    break
            if stuck == deque() or stuck[-1][0] < hist[w]:
                stuck.append([hist[w],rect[1]])
            

print(max_S)
                







