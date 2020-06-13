import bisect
from collections import deque

n = int(input())
Ps = []
for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    if x1 == x2:
        if y2 < y1:
            y1,y2 = y2,y1
        """
        水平線内の点を数える前に垂直線の始点をリストに追加して、
        数えた後に垂直線の終点を取り除くように0,1,2を付与
        """
        Ps.append((y1,x1,"s",0))
        Ps.append((y2,x1,"g",2))

    else:
        if x2 < x1:
            x1,x2 = x2,x1
        Ps.append((y1,x1,x2,1))
Ps.sort(key=lambda x:x[3])
Ps.sort(key=lambda x:x[0])
N = len(Ps)
ans = 0
X = deque()

for i in range(N):
    query = Ps[i]
    if query[2] == "s":
        X.insert(bisect.bisect_left(X,query[1]), query[1])
    elif query[2] == "g":
        del X[bisect.bisect_left(X,query[1])]
    else:
        ans += bisect.bisect_left(X,query[1]) - bisect.bisect_right(X,query[2])

print(-ans)
