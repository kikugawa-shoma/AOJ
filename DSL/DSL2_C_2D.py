import heapq

n = int(input())
Points = [list(map(int,input().split())) for _ in range(n)]
q = int(input())
rectangles = [list(map(int,input().split())) for _ in range(q)]

class BST:
    def __init__(self,A):
        self.n = len(A)
        self.P = A
        self.location = [0]*self.n
        self.l = [0]*self.n
        self.r= [0]*self.n
        self.cnt = 0
        self.d = {}
        self.point_locater()
        self.make2Dtree(0,n,0)

    def point_locater(self):
        for i in range(self.n):
            self.d[tuple(self.P[i])] = i
    
    def make2Dtree(self,l,r,even0_odd1):
        if not l < r:
            return None
        
        mid = (l + r) // 2

        t = self.cnt
        self.cnt += 1

        if even0_odd1 == 0:
            self.P[l:r] = sorted(self.P[l:r],key=lambda x:x[0])
        else:
            self.P[l:r] = sorted(self.P[l:r],key=lambda x:x[1])

        next_even0_odd1 = 1-even0_odd1

        self.location[t] = mid
        self.l[t] = self.make2Dtree(l,mid,next_even0_odd1)
        self.r[t] = self.make2Dtree(mid+1,r,next_even0_odd1)
        return t
    
    def find_ans_clear(self):
        self.find_ans = []
    
    def find(self,v,sx,tx,sy,ty,even0_odd1):
        x = self.P[self.location[v]][0]
        y = self.P[self.location[v]][1]

        if sx <= x <= tx and sy <= y <= ty:
            self.find_ans.append(self.d[(x,y)])
        
        next_evene0_odd1 = 1-even0_odd1
        
        if even0_odd1 == 0:
            if sx <= x and self.l[v] != None:
                self.find(self.l[v],sx,tx,sy,ty,next_evene0_odd1)
            if x <= tx and self.r[v] != None:
                self.find(self.r[v],sx,tx,sy,ty,next_evene0_odd1)
        else:
            if sy <= y and self.l[v] != None:
                self.find(self.l[v],sx,tx,sy,ty,next_evene0_odd1)
            if y <= ty and self.r[v] != None:
                self.find(self.r[v],sx,tx,sy,ty,next_evene0_odd1)

bst = BST(Points)
for i in range(q):
    bst.find_ans_clear()
    bst.find(0,rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3],0)
    bst.find_ans.sort()
    for a in bst.find_ans:
        print(a)
    print("")
