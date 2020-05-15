from collections import deque
q = deque()

n = int(input())
C = [deque() for _ in range(n+1)]

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(tmp[1]):
        C[tmp[0]].append(tmp[2+j])

visited = [False]*(n+1)
d = [0]*(n+1)
f = [0]*(n+1)
t = 0

def stack(i):
    global t
    if visited[i] == False:
        q.append(i)
    while q:
        #¥Î¡¼¥É¤ÎÃµº÷³«»Ï
        node = q[-1]
        if d[node] == 0:
            t += 1
            d[node] = t
        visited[node] = True
        for _ in range(len(C[node])):
            tmp = C[node].popleft()
            if visited[tmp] == False:
                next_node = tmp
                q.append(next_node)    #Ì¤Ãµº÷¤ÎÀÜÂ³¥Î¡¼¥É
                break
        
        #Ì¤Ãµº÷ÀÜÂ³¥Î¡¼¥É¤¬¤Ê¤±¤ì¤Ð¤½¤Î¥Î¡¼¥É¤ÏÃµº÷½ªÎ»
        else:
            t += 1
            f[q.pop()] = t

for i in range(1,n+1):
    stack(i)

for i in range(1,n+1):
    print("{} {} {}".format(i,d[i],f[i]))