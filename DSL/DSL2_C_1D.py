P = [1,3,5,6,10,13,14,16,19,21]
n = len(P)

class BIT:
    def __init__(self,A):
        self.P = A
        self.n = len(A)
        self.location = [0]*n
        self.l = [0]*n
        self.r = [0]*n
        self.cnt = 0
        self.make1DTree(0,n)
    
    def make1DTree(self,l,r):
        if not l < r:
            return None
        
        mid = (l+r) // 2

        t = self.cnt
        self.cnt += 1
        self.location[t] = mid
        self.l[t] = self.make1DTree(l,mid)
        self.r[t] = self.make1DTree(mid+1,r)
        return t
    
    def find_ans_clear(self):
        self.find_ans = []

    def find(self,v,sx,tx):
        x = self.P[self.location[v]]
        if sx <= x <= tx:
            self.find_ans.append(x)

        if sx <= x and self.l[v] != None:
            self.find(self.l[v],sx,tx)
        
        if x <= tx and self.r[v] != None:
            self.find(self.r[v],sx,tx)
    

            


bit = BIT(P)
bit.find_ans_clear()
bit.find(0,6,14)
print(bit.find_ans)

