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

    def __isub__(self, other):
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

    methods
    length()                 :
    get_unit_vec()           : 
    projection(vector)       :
    is_vertical(segment)     :
    is_horizontal(segment)   :
    reflection()             :
    include()                :
    distance()               :
    ccw()                    :
    intersect()              :
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

    def ccw(self,vector):
        """
        線分に対して点が反時計回りの位置にある(1)か時計回りの位置にある(-1)か線分上にある(0)か
        ただし、直線上にはあるが線分上にはない場合は反時計回りの位置にあると判定して1を返す。
        """
        direction = self.v2 - self.v1
        v = vector - self.v1
        if self.include(vector):
            return 0
        else:
            cross = direction**v
            if cross[2] <= 0:
                return 1
            else:
                return -1
    
    def intersect(self,segment):
        """
        線分の交差判定
        """
        ccw12 = self.ccw(segment.v1)
        ccw13 = self.ccw(segment.v2)
        ccw20 = segment.ccw(self.v1)
        ccw21 = segment.ccw(self.v2)

        if ccw12*ccw13*ccw20*ccw21 == 0:
            return True
        else:
            if ccw12*ccw13 < 0 and ccw20*ccw21 < 0:
                return True
            else:
                return False
    
    def intersect_point(self,segment):
        """
        線分の交点
        """
        d1 = norm(self.projection(segment.v1) - segment.v1)
        d2 = norm(self.projection(segment.v2) - segment.v2)
        return segment.v1 + (d1/(d1 + d2)) * (segment.v2 - segment.v1)


class Line(Segment):
    """
    直線クラス
    """
    #直線上に点が存在するか否か
    def include(self,vector):
        proj = self.projection(vector)
        return is_equal(norm(proj-vector),0)
    




q = int(input())
tmp = [0]*q
for i in range(q):
    tmp[i] = list(map(int,input().split()))

for i in range(q):
    p0,p1,p2,p3 = Vector(tmp[i][0:2]),Vector(tmp[i][2:4]),Vector(tmp[i][4:6]),Vector(tmp[i][6:8])
    S1 = Segment(p0,p1)
    S2 = Segment(p2,p3)
    print(*S1.intersect_point(S2))
    