from collections import deque

N,Q=map(int,input().split())
name_time=[[0]*2 for _ in range(N)]
for i in range(N):
    tmp=input().split()
    name_time[i][0]=tmp[0]
    name_time[i][1]=tmp[1]

q=deque()
q.extend(name_time)
now=0
while q:
    tmp=q.popleft()
    name=tmp[0]
    time=int(tmp[1])
    if time <= Q:
        now += time
        print(name,now)
    else:
        now += Q
        time -= Q
        q.append([name,time])


