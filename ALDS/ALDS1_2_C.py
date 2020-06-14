N=int(input())
tmp = input().split()
A=[0]*N
ind=[0]*N
for i in range(N):
    card=tmp[i]
    A[i]=int(card[1])
    ind[i]=i

def BubbleSort(A,N):
    A_bubble=A[:]
    ind_bubble=ind[:]
    flag=1
    while flag:
        flag=0
        j=0
        for i in range(N-1-j):
            if A_bubble[i] > A_bubble[i+1]:
                a=A_bubble[i]
                A_bubble[i]=A_bubble[i+1]
                A_bubble[i+1]=a
                flag=1
                a=ind_bubble[i]
                ind_bubble[i]=ind_bubble[i+1]
                ind_bubble[i+1]=a
    return ind_bubble


def SelectionSort(A,N):
    A_selection=A[:]
    ind_selection=ind[:]
    for i in range(N):
        mini=i
        for j in range(i+1,N):
            if A_selection[j] < A_selection[mini]:
                mini=j
        if mini != i:
            a=A_selection[i]
            A_selection[i]=A_selection[mini]
            A_selection[mini]=a
            a=ind_selection[i]
            ind_selection[i]=ind_selection[mini]
            ind_selection[mini]=a
    return ind_selection


i_b=BubbleSort(A,N)
i_s=SelectionSort(A,N)
ans_b=[]
ans_s=[]
for i in range(N):
    ans_b.append("".join([tmp[i_b[i]][0],tmp[i_b[i]][1]]))
    ans_s.append("".join([tmp[i_s[i]][0],tmp[i_s[i]][1]]))

print(*ans_b)
print("Stable")
print(*ans_s)
if ans_b != ans_s:
    print("Not stable")
else:
    print("Stable")
