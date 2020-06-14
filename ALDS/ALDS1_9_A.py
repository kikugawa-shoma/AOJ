n = int(input())
A = list(map(int,input().split()))
A.insert(0,-1)

for i in range(1,n+1):
    print("node {}: ".format(i),end = "")

    print("key = {}, ".format(A[i]),end = "")

    if (i // 2) > 0:
        print("parent key = {}, ".format(A[i // 2]),end = "")
    
    if 2*i <= n:
        print("left key = {}, ".format(A[2*i]),end = "")
    
    if 2*i + 1 <= n:
        print("right key = {}, ".format(A[2*i + 1]),end = "")
    
    print("")



    
        

