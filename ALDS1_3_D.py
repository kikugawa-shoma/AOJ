from collections import deque

S = input()

pool_q=deque()
slope_q=deque()

for i,s in enumerate(S):
    if s=="\\":
        slope_q.append(i)
        pool_q.append((i,0))
    elif s=="/":
        if len(slope_q) > 0:
            pre_down=slope_q.pop()
            plus=i-pre_down
            while 1:
                pre_pool=pool_q.pop()
                if pre_pool[0] == pre_down:
                    pool_q.append((pre_down,plus))
                    break
                else:
                    plus+=pre_pool[1]
SUM = 0
ans=[0]
cnt=0
for i in range(len(pool_q)):
    pool=pool_q.popleft()[1]
    if pool > 0:
        ans.append(pool)
        SUM+=pool
        cnt+=1
ans[0]=cnt
print(SUM)
print(*ans)