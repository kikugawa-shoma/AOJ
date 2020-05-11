n = int(input())
inst_k = [-1]*n
inst = [-1]*n
for i in range(n):
    tmp = input().split()
    inst[i] = tmp[0]
    if len(tmp) == 2:
        inst_k[i] = int(tmp[1])

class BST:
    def __init__(self):
        self.key = []
        self.parent = []
        self.left_child = []
        self.right_child = []
        self.root = None

    def insert(self,new_key):
        new_node = len(self.key)
        self.key.append(new_key)
        self.left_child.append(None)
        self.right_child.append(None)
        self.parent.append(None)

        searching_node = self.root
        searching_node_parent = None
        while searching_node != None:
            searching_node_parent = searching_node
            if new_key < self.key[searching_node]:
                searching_node = self.left_child[searching_node]
            else:
                searching_node = self.right_child[searching_node]
        if searching_node_parent == None:
            self.root = new_node
        else:
            self.parent[new_node] = searching_node_parent
            if new_key < self.key[searching_node_parent]:
                self.left_child[searching_node_parent] = new_node
            else:
                self.right_child[searching_node_parent] = new_node
    
    def print_clear(self):
        self.preorder_ans = []
        self.inorder_ans = []
    
    def preorder(self,node):
        if node != None:
            self.preorder_ans.append(self.key[node])
            self.preorder(self.left_child[node])
            self.preorder(self.right_child[node])
    
    def inorder(self,node):
        if node != None:
            self.inorder(self.left_child[node])
            self.inorder_ans.append(self.key[node])
            self.inorder(self.right_child[node])
    
    def find(self,key,node):
        if node == None:
            return None
        else:
            if self.key[node] == key:
                return node
            else:
                if key < self.key[node]:
                    return self.find(key,self.left_child[node])
                else:
                    return self.find(key,self.right_child[node])
     
    def delete(self,key):
        del_node = self.find(key,self.root)
        if self.left_child[del_node] == None or self.right_child[del_node] == None:
            instead_node = del_node
        else:
            instead_node = self.getSuccessor(del_node)
        
        if self.left_child[instead_node] != None:
            instead_node_child = self.left_child[instead_node]
        else:
            instead_node_child = self.right_child[instead_node]
        
        if instead_node_child != None:
            self.parent[instead_node_child] = self.parent[instead_node]

        if self.root == instead_node:
            self.root = instead_node_child
        elif self.left_child[self.parent[instead_node]] == instead_node:
            self.left_child[self.parent[instead_node]] = instead_node_child
        else:
            self.right_child[self.parent[instead_node]] = instead_node_child
        
        if instead_node != del_node:
            self.key[del_node] = self.key[instead_node]

    def getSuccessor(self,node):
        if self.right_child[node] != None:
            return self.getMinimum(self.right_child[node])
        else:
            ret = node
            while self.left_child[self.parent[ret]] != ret and ret != None:
                ret = self.parent[ret]
            return self.parent[ret]
    
    def getMinimum(self,node):
        while self.left_child[node] != None:
            node = self.left_child[node]
        return node

tree = BST()
for i in range(n):
    if inst[i] == "insert":
        tree.insert(inst_k[i])

    elif inst[i] == "find":
        if tree.find(inst_k[i],tree.root) != None:
            print("yes")
        else:
            print("no")

    elif inst[i] == "delete":
        tree.delete(inst_k[i])

    elif inst[i] == "print":
        tree.print_clear()
        tree.preorder(tree.root)
        tree.inorder(tree.root)
        print(" ",end = "")
        print(*tree.inorder_ans)
        print(" ",end = "")
        print(*tree.preorder_ans)
