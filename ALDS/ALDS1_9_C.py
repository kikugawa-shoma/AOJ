"""
TLE
"""

order = [-1]
ks = [-1]

while order[-1] != "end":
    tmp = input().split()
    order.append(tmp[0])
    if tmp[0] == "insert":
        ks.append(int(tmp[1]))
    else:
        ks.append(-1)

class PriorityQueue:
    def __init__(self):
        self.heap = [-1]
        self.l = 0
    
    def insert(self,key):
        self.heap.append(key)
        self.l += 1
        i = self.l
        while self.parent(i) and key > self.heap[self.parent(i)]:
            self.heap[self.parent(i)],self.heap[i] = self.heap[i],self.heap[self.parent(i)]
            i = self.parent(i)
    
    def extractmax(self):
        ans = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        self.l -= 1
        self.maxheapify(1)
        return ans

    def maxheapify(self,i):
        left_child = self.left_child(i)
        right_child = self.right_child(i)
        larger = i
        if left_child and self.heap[larger] < self.heap[left_child]:
            larger = left_child
        if right_child and self.heap[larger] < self.heap[right_child]:
            larger = right_child
        
        if larger != i:
            self.heap[larger],self.heap[i] = self.heap[i],self.heap[larger]
            self.maxheapify(larger)
    
    def parent(self,i):
        if i != 1:
            return i // 2
        else:
            return False
    
    def left_child(self,i):
        if 2*i <= self.l:
            return 2*i
        else:
            return False

    def right_child(self,i):
        if 2*i+1 <= self.l:
            return 2*i+1
        else:
            return False

q = PriorityQueue()
for i in range(1,len(ks)):
    if order[i] == "insert":
        q.insert(ks[i])
    elif order[i]  == "extract":
        print(q.extractmax())
    elif order[i] == "end":
        break



