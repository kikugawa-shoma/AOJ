n=int(input())
A=tuple(map(int,input().split()))
cnt=0
def merge_sort(A,n):
    if n == 1:
        return A
    else:
        global cnt
        mid=(n+1)//2
        nl=len(A[:mid])
        nr=len(A[mid:])
        L=merge_sort(A[:mid],nl)
        R=merge_sort(A[mid:],nr)
        nli=0
        nri=0
        ans=[0]*(nl+nr)
        i=0
        while i < n:
            if nli == nl:
                ans[i]=R[nri]
                nri += 1
            elif nri == nr:
                ans[i]=L[nli]
                nli += 1
            elif L[nli] <= R[nri]:
                ans[i]=L[nli]
                nli += 1
            else:
                ans[i]=R[nri]
                nri += 1
                cnt += nl-nli
            i += 1
        return tuple(ans)
                



merge_sort(A,n)
print(cnt)
