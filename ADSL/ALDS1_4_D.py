n,k=map(int, input().split())
w=[0]*n
for i in range(n):
    w[i]=int(input())

def delivable(m):
    loading=0
    track_num=1
    for i in range(n):
        if w[i] > m:
            return False
            break
        else:
            loading += w[i] 
            if loading > m:
                loading=w[i]
                track_num += 1
    if track_num <= k:
        return True
    else:
        return False


r=1000000000
l=min(w)-1
while r-l > 1:
    m=(r+l)//2
    if delivable(m):
        r=m
    else:
        l=m

print(r)
