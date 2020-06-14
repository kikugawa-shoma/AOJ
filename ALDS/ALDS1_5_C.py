import math
n=int(input())

def add_v(l1,l2):
    n=len(l1)
    l=[0]*n
    for i in range(n):
        l[i]=l1[i]+l2[i]
    return l

def scar_multiple_v(scalar,l):
    n=len(l)
    ans=[0]*n
    for i in range(n):
        ans[i]=l[i]*scalar
    return ans

def mat_multi_v(mat,l):
    n=len(l)
    ans=[0]*n
    for i in range(n):
        for j in range(n):
            ans[i]+=mat[i][j]*l[j]
    return ans

def make_points(tail,head):
    ans=[[0]*2 for _ in range(5)]
    ans[0]=tuple(tail)
    ans[1]=tuple(add_v(tail,scar_multiple_v(1/3,add_v(head,scar_multiple_v(-1,tail)))))

    v=scar_multiple_v(1/3,add_v(head,scar_multiple_v(-1,tail)))
    mat=[[1+math.cos(math.radians(60)),-math.sin(math.radians(60))],\
         [math.sin(math.radians(60))  ,1+math.cos(math.radians(60))]]
    ans[2]=tuple(add_v(tail,mat_multi_v(mat,v)))
    ans[3]=tuple(add_v(tail,scar_multiple_v(2/3,add_v(head,scar_multiple_v(-1,tail)))))
    ans[4]=tuple(head)
    return tuple(ans)

def make_1_coch_curve(iter,tail,head):
    points=make_points(tail,head)
    if iter == n-1:
        for i in range(len(points)-1):
            print("{} {}".format(points[i][0],points[i][1]))
            
    else:
        for i in range(4):
            make_1_coch_curve(iter+1,points[i],points[i+1])
            
if n == 0:
    print("{} {}\n{} {}".format(0,0,100,0))
else:
    make_1_coch_curve(0,[0,0],[100,0])
    print("{} {}".format(100,0))
        
