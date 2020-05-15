from collections import defaultdict

n=int(input())
cards=[0]*n
A=[0]*n
inds=[0]*n
d=defaultdict(lambda :[])
di=defaultdict(int)
for i in range(n):
    tmp=input().split()
    cards[i]=tmp[0],int(tmp[1])
    A[i]=int(tmp[1])
    inds[i]=i
    d[int(tmp[1])].append(tmp[0])

def partition(A,inds,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j] <= x:
            i+=1
            A[i],A[j]=A[j],A[i]
            inds[i],inds[j]=inds[j],inds[i]
    A[i+1],A[r]=A[r],A[i+1]
    inds[i+1],inds[r]=inds[r],inds[i+1]
    return i+1

def quicksort(A,inds,p,r):
    if p < r:
        q=partition(A,inds,p,r)
        quicksort(A,inds,p,q-1)
        quicksort(A,inds,q+1,r)

quicksort(A,inds,0,n-1)

stable_flag=True
for i in range(n):
    num_i=cards[inds[i]][1]
    suit=cards[inds[i]][0]

    if d[num_i][di[num_i]] != suit:
        stable_flag=False
        break
    di[num_i]+=1

if stable_flag:
    print("Stable")
else:
    print("Not stable")

for i in range(n):
    print(*cards[inds[i]])

