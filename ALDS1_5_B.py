n=int(input())
A=tuple(map(int, input().split()))
cnt=0

def merge_sort(A,cnt):
    m=len(A)
    if m == 1:
        return A,cnt
    else:
        mid=(m+1)//2
        A1=tuple(A[:mid])
        A2=tuple(A[mid:])
        A1,cnt=merge_sort(A1,cnt)
        A2,cnt=merge_sort(A2,cnt)
        n1=len(A1)
        n2=len(A2)
        i1=0
        i2=0
        ans=[0]*(n1+n2)
        j=0
        while j < n1+n2:
            if i1 == n1:
                ans[j]=A2[i2]
                i2+=1
                cnt+=1
            elif i2 == n2:
                ans[j]=A1[i1]
                i1+=1
                cnt+=1
            elif A1[i1] < A2[i2]:
                ans[j]=A1[i1]
                i1+=1
                cnt+=1
            else:
                ans[j]=A2[i2]
                i2+=1
                cnt+=1
            j += 1
        return ans,cnt

sorted_A,cnt=merge_sort(A,0)
print(*sorted_A)
print(cnt)

            

        