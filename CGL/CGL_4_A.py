"""
TLE
"""
from collections import deque
import math
EPS = 10**(-9)
def is_equal(a,b):
    return abs(a-b) < EPS

def norm(v,i=2):
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
    def angle(self):
        if len(self) != 2:
            return False
        else:
            if is_equal(super().__getitem__(0), 0) and is_equal(super().__getitem__(1), 0):
                return False
            elif is_equal(super().__getitem__(0), 0):
                if super().__getitem__(1) > 0:
                    return math.pi/2
                elif super().__getitem__(1) < 0:
                    return -math.pi/2
            else:
                if super().__getitem__(0) > 0:
                    return math.atan(super().__getitem__(1)/super().__getitem__(0))
                elif super().__getitem__(0) < 0:
                    return math.atan(super().__getitem__(1)/super().__getitem__(0)) + math.pi


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
    intersect_point          :
    """
    def __init__(self,v1,v2):
        if v2[0] < v1[0]:
            v1,v2 = v2,v1
        self.v1 = v1
        self.v2 = v2
    

    def ccw(self,vector):
        """
        線分に対して点が反時計回りの位置にある(1)か時計回りの位置にある(-1)か線分上にある(0)か
        ただし、直線上にはあるが線分上にはない場合は反時計回りの位置にあると判定して1を返す。
        """
        direction = self.v2 - self.v1
        v = vector - self.v1
        cross = direction**v
        if cross[2] <= 0:
            return 1
        else:
            return -1

    def ccw_(self,vector):
        """
        線分に対して点が反時計回りの位置にある(1)か時計回りの位置にある(-1)か線分上にある(0)か
        ただし、直線上にはあるが線分上にはない場合は反時計回りの位置にあると判定して1を返す。
        """
        direction = self.v2 - self.v1
        v = vector - self.v1
        cross = direction**v
        if cross[2] < 0:
            return 1
        else:
            return -1   




n = int(input())
points = [0]*n
for i in range(n):
    points[i] = Vector(list(map(int,input().split())))

points.sort()
q = deque()
q.append(points[0])
q.append(points[1])

for i in range(2,n):
    now_p = points[i] 
    while 1:
        p_l = q[-1]
        p_s = q[-2]
        L = Segment(p_s,p_l)
        if L.ccw(now_p) == 1:
            q.append(now_p)
            break
        else:
            q.pop()
        if len(q) < 2:
            q.append(now_p)
            break
upper = list(q)[:]

q = deque()
q.append(points[0])
q.append(points[1])
for i in range(2,n):
    now_p = points[i] 
    while 1:
        p_l = q[-1]
        p_s = q[-2]
        L = Segment(p_s,p_l)
        if L.ccw_(now_p) == -1:
            q.append(now_p)
            break
        else:
            q.pop()
        if len(q) < 2:
            q.append(now_p)
            break
lower = list(q)[:]

sorted_lower = sorted(lower,key=lambda x:x[1])
first = sorted_lower[0]
first_ind = lower.index(first)
print(len(lower)+len(upper)-2)

for i in range(first_ind,len(lower)):
    print(*lower[i])
for i in range(len(upper)-2,0,-1):
    print(*upper[i])
for i in range(first_ind):
    print(*lower[i])

