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

n = int(input())
Ps = [Vector(list(map(int,input().split()))) for _ in range(n)]
Ps.sort()

qu = deque()
qd = deque()
qu.append(Ps[0])
qu.append(Ps[1])
qd.append(Ps[0])
qd.append(Ps[1])

for i in range(2,n):
    now_p = Ps[i]
    while 1:
        vul = qu[-1] - qu[-2]
        vus = now_p - qu[-2]
        cross_u = vul**vus
        if cross_u[2] > 0:
            qu.pop()
        else:
            qu.append(now_p)
            break
        if len(qu) < 2:
            qu.append(now_p)
            break

    while 1:
        vdl = qd[-1] - qd[-2]
        vds = now_p - qd[-2]
        cross_d = vdl**vds
        if cross_d[2] < 0:
            qd.pop()
        else:
            qd.append(now_p)
            break
        if len(qd) < 2:
            qd.append(now_p)
            break

y_min_ans = min(qd,key=lambda x:x[1])
min_ind = qd.index(y_min_ans)

print(len(qu)+len(qd)-2)
for i in range(min_ind,len(qd)):
    print(*qd[i])
for i in range(len(qu) - 2,0,-1):
    print(*qu[i])
for i in range(min_ind):
    print(*qd[i])


        






