H = int(input())
A = list(map(int, input().split()))

class HeapTree:
    def __init__(self,A):
        self.heap = [-1] + A
        self.l = len(self.heap)-1
        self.buildMaxHeap()


    def maxHeapify(self,i):
        left_child = self.left_child(i)
        right_child = self.right_child(i)
        larger = i
        if left_child and self.heap[left_child] > self.heap[i]:
            larger = left_child
        if right_child and self.heap[right_child] > self.heap[larger]:
            larger = right_child
        
        if larger != i:
            tmp = self.heap[i]
            self.heap[i] = self.heap[larger]
            self.heap[larger] = tmp
            self.maxHeapify(larger)

    def parent(self,i):
        return i//2

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
    
    def buildMaxHeap(self):
        max_ind_parent = self.parent(self.l)
        for i in range(max_ind_parent,0,-1):
            self.maxHeapify(i)

heap_tree = HeapTree(A)
print(" ",end="")
print(*heap_tree.heap[1:])

