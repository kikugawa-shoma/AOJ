n=int(input())
S=list(map(int,input().split()))
q=int(input())
T=list(map(int, input().split()))

def bin_search(t):
    l=0
    r=n-1
    if S[r]==t:
        return 1
    else:
        while r-l > 1:
            m=(l+r)//2
            if S[m] > t:
                r=m
            else:
                l=m
        if S[l] == t:
            return 1
        else:
            return 0

cnt=0
for t in T:
    cnt += bin_search(t)

print(cnt)
