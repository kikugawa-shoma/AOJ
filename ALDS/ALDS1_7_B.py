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
        self.d=[0]*self.n
        self.degree=[0]*self.n
        self.sibling=[-1]*self.n
        self.node_type=[0]*self.n
        self.height=[-1]*self.n

    def set_depth(self,id,d):
        if id != -1:
            self.d[id]=d
            self.set_depth(self.left_child[id],d+1)
            self.set_depth(self.right_child[id],d+1)
    
    def set_degree(self):
        for i in range(self.n):
            deg=0
            if self.left_child[i] != -1:
                deg += 1
            if self.right_child[i] != -1:
                deg += 1
            self.degree[i]=deg
    
    def set_sibling(self):
        for i in range(self.n):
            if self.right_child[i] != -1 and self.left_child[i] != -1:
                self.sibling[self.right_child[i]]=self.left_child[i]
                self.sibling[self.left_child[i]]=self.right_child[i]
    
    def set_height(self,id):
        if self.left_child[id] == -1 and self.right_child[id] == -1:
            self.height[id]=0
        else:
            h1=self.set_height(self.left_child[id])
            h2=self.set_height(self.right_child[id])
            self.height[id]=max(h1,h2)+1
        return self.height[id]


    
    def set_node_type(self):
        for i in range(self.n):
            if self.parent[i] == -1:
                self.node_type[i]="root"
            elif self.left_child[i] == -1 and self.right_child[i] == -1:
                self.node_type[i]="leaf"
            else:
                self.node_type[i]="internal node"
    
tree = BisectTree(childs)
tree.set_sibling()
tree.set_degree()
tree.set_depth(tree.root,0)
tree.set_height(tree.root)
tree.set_node_type()

for i in range(n):
    print("node {}: ".format(i),end="")
    print("parent = {}, ".format(tree.parent[i]),end="")
    print("sibling = {}, ".format(tree.sibling[i]),end="")
    print("degree = {}, ".format(tree.degree[i]),end="")
    print("depth = {}, ".format(tree.d[i]),end="")
    print("height = {}, ".format(tree.height[i]),end="")
    print(tree.node_type[i])


            

            
    