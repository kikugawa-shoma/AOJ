import sys
sys.setrecursionlimit(100010)
n=int(input())
childs_list=[[] for _ in range(n)]
for i in range(n):
    tmp=list(map(int, input().split()))
    childs_num=tmp[1]
    node_id=tmp[0]
    childs_list[node_id].extend(tmp[2:])

class Tree:
    def __init__(self,childs_list):
        self.n=len(childs_list)
        self.parent=[-1]*self.n
        self.first_child=[-1]*self.n
        self.next_child=[-1]*self.n
        for i in range(self.n):
            childs_num=len(childs_list[i])
            if childs_num == 0:
                continue
            self.first_child[i]=childs_list[i][0]
            for j in range(childs_num):
                self.parent[childs_list[i][j]]=i
                if j < childs_num-1:
                    self.next_child[childs_list[i][j]]=childs_list[i][j+1]
        self.node_type=[0]*n
        for i in range(self.n):
            if self.parent[i]==-1:
                self.node_type[i]="root"
                self.root=i
            elif self.first_child[i]==-1:
                self.node_type[i]="leaf"
            else:
                self.node_type[i]="internal node"
        self.d=[-1]*self.n

    def parent_of(self,id):
        return self.parent[id]
    
    def childs_of(self,id):
        childs=[]
        if self.first_child[id]==-1:
            return childs
        else:
            now_child=self.first_child[id]
            while 1:
                childs.append(now_child)
                if self.next_child[now_child] == -1:
                    break
                else:
                    now_child=self.next_child[now_child]
        return childs
    
    def set_depth(self,id,d):
        if id != -1:
            self.d[id]=d
            self.set_depth(self.next_child[id],d)
            self.set_depth(self.first_child[id],d+1)


tree=Tree(childs_list)
tree.set_depth(tree.root,0)

for i in range(n):
    print("node {}: ".format(i),end="")
    print("parent = {}, ".format(tree.parent_of(i)),end="")
    print("depth = {}, ".format(tree.d[i]),end="")
    print("{}, ".format(tree.node_type[i]),end="")
    print(tree.childs_of(i))
