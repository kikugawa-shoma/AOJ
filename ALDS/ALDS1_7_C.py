n=int(input())
childs=[0]*n

for i in range(n):
    node=list(map(int,input().split()))
    childs[node[0]] = node[1:]

class BisectTree:
    def __init__(self,childs):
        self.n=len(childs) 
        self.left_child=[0]*self.n
        self.right_child=[0]*self.n
        self.parent=[-1]*self.n
        for i in range(self.n):
            self.left_child[i]=childs[i][0]
            self.right_child[i]=childs[i][1]
            if childs[i][0] != -1:
                self.parent[childs[i][0]]=i
            if childs[i][1] != -1:
                self.parent[childs[i][1]]=i
        self.root=self.parent.index(-1)

tree=BisectTree(childs)

def preorder(tree,node,ans):
    ans.append(node)
    left=tree.left_child[node]
    right=tree.right_child[node]
    if left != -1:
        preorder(tree,left,ans)
    if right != -1:
        preorder(tree,right,ans)

def inorder(tree,node,ans):
    left=tree.left_child[node]
    right=tree.right_child[node]
    if left != -1:
        inorder(tree,left,ans)
    ans.append(node)
    if right != -1:
        inorder(tree,right,ans)

def postorder(tree,node,ans):
    left=tree.left_child[node]
    right=tree.right_child[node]
    if left != -1:
        postorder(tree,left,ans)
    if right != -1:
        postorder(tree,right,ans)
    ans.append(node)
    

preorder_ans=[]
preorder(tree,tree.root,preorder_ans)
print("Preorder\n ",end="")
print(*preorder_ans)

inorder_ans=[]
inorder(tree,tree.root,inorder_ans)
print("Inorder\n ",end="")
print(*inorder_ans)

postorder_ans=[]
postorder(tree,tree.root,postorder_ans)
print("Postorder\n ",end="")
print(*postorder_ans)


