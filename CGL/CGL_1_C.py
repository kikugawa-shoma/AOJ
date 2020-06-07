EPS = 10**(-9)
def is_equal(a,b):
    return abs(a-b) < EPS

def norm(v,i=2):
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
    /  : スカラー除法
    ** : 外積
    += : ベクトル和
    -= : ベクトル差
    *= : スカラー倍
    /= : スカラー除法

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
                return ret
            else:
                return ret

class Segment:
    """
    線分クラス
    """
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    
    def length(self):
        return norm(self.v1-self.v2)

    def get_unit_vec(self):
        #方向単位ベクトル
        dist = norm(self.v2-self.v1)
        if dist != 0:
            return (self.v2-self.v1)/dist
        else:
            return False
    
    def projection(self,vector):
        #射影点(線分を直線と見たときの)
        unit_vec = self.get_unit_vec()
        t = unit_vec*(vector-self.v1)
        return self.v1 + t*unit_vec
    
    def is_vertical(self,other):
        #線分の直交判定
        return is_equal(0,self.get_unit_vec()*other.get_unit_vec())
    
    def is_horizontal(self,other):
        #線分の平行判定
        return is_equal(0,self.get_unit_vec()**other.get_unit_vec())
    
    def reflection(self,vector):
        #反射点(線分を直線と見たときの)
        projection = self.projection(vector)
        v = projection - vector
        return projection + vector
    
    def include(self,vector):
        #線分が点を含むか否か
        proj = self.projection(vector)
        if not is_equal(norm(proj-vector),0):
            return False
        else:
            n = len(self.v1)
            f = True
            for i in range(n):
                f &= ((self.v1[i] <= vector[i] <= self.v2[i]) or (self.v2[i] <= vector[i] <=self.v1[i]))
            return f
    
    def distance(self,other):
        #点と線分の距離
        if isinstance(other,Vector):
            proj = self.projection(other)
            if self.include(proj):
                return norm(proj-other)
            else:
                ret = []
                ret.append(norm(self.v1-other))
                ret.append(norm(self.v2-other))
                return min(ret)


class Line(Segment):
    """
    直線クラス
    """
    #直線上に点が存在するか否か
    def include(self,vector):
        proj = self.projection(vector)
        return is_equal(norm(proj-vector),0)

xp0,yp0,xp1,yp1 = map(int,input().split())
p0 = Vector([xp0,yp0])
p1 = Vector([xp1,yp1])
p01 = p1-p0
q = int(input())
p2s = [0]*q
p02s = [0]*q
L01 = Line(p0,p1)
S01 = Segment(p0,p1)
for i in range(q):
    p2s[i] = Vector(list(map(int,input().split())))
    p02s[i] = p2s[i]-p0

ans = [0]*q
for i in range(q):
    p02 = p02s[i]
    p2 = p2s[i]
    S21 = Segment(p2,p1)
    S02 = Segment(p0,p2)
    if L01.include(p2):
        if S01.include(p2):
                ans[i] = "ON_SEGMENT"
        elif S02.length != 0 and S02.include(p1):
            ans[i] = "ONLINE_FRONT"
        elif S21.length != 0 and S21.include(p0):
            ans[i] = "ONLINE_BACK"
    else:
        cross = p01**p02
        if cross[2] > 0:
            ans[i] = "COUNTER_CLOCKWISE"
        else:
            ans[i] = "CLOCKWISE"

for i in range(q):
    print(ans[i])









