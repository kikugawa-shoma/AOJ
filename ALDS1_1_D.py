N=int(input())
R=[int(input()) for i in range(N)]
max_prifit=R[1]-R[0]
minR=R[0]
for i in range(1,N):
    max_prifit=max(max_prifit,R[i]-minR)
    minR=min(minR, R[i])

print(max_prifit)

