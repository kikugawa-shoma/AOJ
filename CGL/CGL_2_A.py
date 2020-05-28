EPS = 10**(-9)
def is_equal(a,b):
    return abs(a-b) < EPS

def norm(v,i):
    import math
    ret = 0
    n = len(v)
    for j in range(n):
        ret += abs(v[j])**i
    return math.pow(ret,1/i)

class Vector(list):
    def __add__(self,other):
        n = len(self)
        ret = [0]*n
        for i in range(n):
            ret[i] = super().__getitem__(i) + other.__getitem__(i)
        return self.__class__(ret)
    
    def __radd__(self,other):
        n = len(self)
        ret = [0]*n
        for i in range(n):
            ret[i] = other.__getitem__(i) + super().__getitem__(i)
        return self.__class__(ret)
    
    def __iadd__(self, other):
        n = len(self)
        for i in range(n):
            self[i] += other.__getitem__(i)
        return self

    def __sub__(self,others):
        n = len(self) 
        ret = [0]*n
        for i in range(n):
            ret[i] = super().__getitem__(i) - others.__getitem__(i)
        return self.__class__(ret)

    def __iadd__(self, other):
        n = len(self)
        for i in range(n):
            self[i] -= other.__getitem__(i)
        return self

    def __rsub__(self,others):
        n = len(self) 
        ret = [0]*n
        for i in range(n):
            ret[i] = others.__getitem__(i) - super().__getitem__(i)
        return self.__class__(ret)
    
    def __mul__(self,other):
        n = len(self)
        if isinstance(other,list):
            ret = 0
            for i in range(n):
                ret += super().__getitem__(i)*other.__getitem__(i)
            return ret
        else:
            ret = [0]*n
            for i in range(n):
                ret[i] = super().__getitem__(i)*other
            return self.__class__(ret)

    def __rmul__(self,other):
        n = len(self)
        if isinstance(other,list):
            ret = 0
            for i in range(n):
                ret += super().__getitem__(i)*other.__getitem__(i)
            return ret
        else:
            ret = [0]*n
            for i in range(n):
                ret[i] = super().__getitem__(i)*other
            return self.__class__(ret)
    
    
    def __truediv__(self,other):
        n = len(self)
        ret = [0]*n
        for i in range(n):
            ret[i] = super().__getitem__(i)/other
        return self.__class__(ret)
    
    def norm(self,i):
        return norm(self,i)
    
    def __pow__(self,other):
        n = len(self)
        ret = [0]*3
        x = self[:]
        y = other[:]
        if n == 2:
            x.append(0)
            y.append(0)
        if n == 2 or n == 3:
            for i in range(3):
                ret[0],ret[1],ret[2] = x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]
            ret = Vector(ret)
            if n == 2:
                return ret.norm(2)
            else:
                return ret

class Segment:
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

class Line(Segment):
    def get_unit_vec(self):
        return (self.v1-self.v2)/norm(self.v1-self.v2,2)
    
    def is_vertical(self,other_line):
        return is_equal(0,self.get_unit_vec()*other_line.get_unit_vec())
    
    def is_horizontal(self,other_line):
        return is_equal(0,self.get_unit_vec()**other_line.get_unit_vec())


q = int(input())
for _ in range(q):
    tmp = list(map(int,input().split()))
    vectors = [0]*4
    for j in range(4):
        vectors[j] = Vector(tmp[j*2:(j+1)*2])
    l1 = Line(vectors[0],vectors[1])
    l2 = Line(vectors[2],vectors[3])

    if l1.is_horizontal(l2):
        print(2)
    elif l1.is_vertical(l2):
        print(1)
    else:
        print(0)

