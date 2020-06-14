N=int(input())
preorder=list(map(int,input().split()))
inorder=list(map(int,input().split()))
pre_iter=iter(preorder)
bisect_tree = [[None,None] for i in range(N+1)]

def reconst(l,r):
    global pre_iter
    if r-l <= 0:
        return
    if r-l == 1:
        next(pre_iter)
        return inorder[l]
    partial_root = next(pre_iter)
    partial_root_position = inorder.index(partial_root)
    left_child = reconst(l,partial_root_position)
    right_child = reconst(partial_root_position+1,r)
    bisect_tree[partial_root][0]=left_child
    bisect_tree[partial_root][1]=right_child
    return partial_root
ans=[]
def postorder(node):
    if bisect_tree[node] == [None,None]:
        ans.append(node)
    else:
        if bisect_tree[node][0] != None:
            postorder(bisect_tree[node][0])
        if bisect_tree[node][1] != None:
            postorder(bisect_tree[node][1])
        ans.append(node)

def root_search():
    parent=[-1]*(N+1)
    for i in range(1,N+1):
        if bisect_tree[i][0] != None:
            parent[bisect_tree[i][0]]=i
        if bisect_tree[i][1] != None:
            parent[bisect_tree[i][1]]=i
    for i in range(1,N+1):
        if parent[i] == -1:
            break
    return i

reconst(0,N)
root = root_search()
postorder(root)
print(*ans)