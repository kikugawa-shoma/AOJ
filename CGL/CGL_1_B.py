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
    """
    ベクトルクラス
    対応演算子
    +  : ベクトル和 
    -  : ベクトル差
    *  : スカラー倍、または内積
    ** : 外積
    += : ベクトル和
    -= : ベクトル差
    *= : スカラー倍
    /= : スカラー倍

    メソッド
    self.norm(i) : L{i}ノルムを計算
    """
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
        """
        ベクトルのスカラー除法
        Vector/scalar
        """
        n = len(self)
        ret = [0]*n
        for i in range(n):
            ret[i] = super().__getitem__(i)/other
        return self.__class__(ret)
    
    def norm(self,i):
        """
        L{i}ノルム
        self.norm(i)
        """
        return norm(self,i)
    
    def __pow__(self,other):
        """
        外積
        self**other
        """
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
    """
    線分クラス
    """
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

class Line(Segment):
    """
    直線クラス
    """
    def get_unit_vec(self):
        return (self.v2-self.v1)/norm(self.v2-self.v1,2)
    
    def projection(self,vector):
        unit_vec = self.get_unit_vec()
        t = unit_vec*(vector-self.v1)
        return self.v1 + t*unit_vec
    
    def is_vertical(self,other):
        return is_equal(0,self.get_unit_vec()*other.get_unit_vec())
    
    def is_horizontal(self,other):
        return is_equal(0,self.get_unit_vec()**other.get_unit_vec())
    
    def reflection(self,vector):
        projection = self.projection(vector)
        v = projection - vector
        return projection + v


xp1,yp1,xp2,yp2 = map(float,input().split())
q = int(input())
ps = [list(map(int,input().split())) for i in range(q)]

p1 = Vector([xp1,yp1])
p2 = Vector([xp2,yp2])
L = Line(p1,p2)

for p in ps:
    ans = L.reflection(p)
    ans = [float(round(a,11)) for a in ans]
    print(*ans)
