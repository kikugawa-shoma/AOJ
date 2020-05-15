n=int(input())
A=list(map(int, input().split()))

def cycle_search(i):
    next_search_ind=i
    ret=[]
    while 1:
        now_ind=next_search_ind
        next_search_ind=sorted_A.index(A[now_ind])
        ret.append(A[now_ind])
        cycle_searched[now_ind]=True
        if cycle_searched[next_search_ind]:
            break
    return ret


sorted_A=sorted(A)

cycles=[]
cycle_searched=[False]*n

for i in range(n):
    if cycle_searched[i] == False:
        cycles.append(cycle_search(i))

ans=0
min_A=sorted_A[0]
for cycle in cycles:
    cycle_len=len(cycle)
    if cycle_len == 1:
        continue
    else:
        ans1 = sum(cycle)+(cycle_len-2)*min(cycle)
        min_cycle=min(cycle)
        ans2 = sum(cycle)-min_cycle+min_A+(cycle_len-2)*min_A+2*(min_A+min_cycle)
        ans += min(ans1,ans2)

print(ans)