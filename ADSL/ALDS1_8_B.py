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
        self.root = -1

    def insert(self,new_key):
        new_node = len(self.key)
        self.key.append(new_key)
        self.left_child.append(-1)
        self.right_child.append(-1)
        self.parent.append(-1)

        searching_node = self.root
        searching_node_parent = -1
        while searching_node != -1:
            searching_node_parent = searching_node
            if new_key < self.key[searching_node]:
                searching_node = self.left_child[searching_node]
            else:
                searching_node = self.right_child[searching_node]
        if searching_node_parent == -1:
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
        if node != -1:
            self.preorder_ans.append(self.key[node])
            self.preorder(self.left_child[node])
            self.preorder(self.right_child[node])
    
    def inorder(self,node):
        if node != -1:
            self.inorder(self.left_child[node])
            self.inorder_ans.append(self.key[node])
            self.inorder(self.right_child[node])
    
    def find(self,key,node):
        if node == -1:
            return None
        else:
            if self.key[node] == key:
                return node
            else:
                if key < self.key[node]:
                    return self.find(key,self.left_child[node])
                else:
                    return self.find(key,self.right_child[node])

tree = BST()
for i in range(n):
    if inst[i] == "insert":
        tree.insert(inst_k[i])
    elif inst[i] == "find":
        if tree.find(inst_k[i],tree.root) != None:
            print("yes")
        else:
            print("no")
    elif inst[i] == "print":
        tree.print_clear()
        tree.preorder(tree.root)
        tree.inorder(tree.root)
        print(" ",end = "")
        print(*tree.inorder_ans)
        print(" ",end = "")
        print(*tree.preorder_ans)
