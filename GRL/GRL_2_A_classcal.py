V,E = map(int,input().split())
edges = [[0,0,0] for _ in range(E)]
for i in range(E):
    s,t,w = map(int,input().split())
    edges[i][0],edges[i][1],edges[i][2] = s,t,w

edges.sort(key=lambda x:x[2])

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i in range(self.n) if self.parents[i] < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())
    
tree = UnionFind(V)
edge_cnt = 0
group_num = V
ans = 0
while group_num > 1:
    s,t,w = edges[edge_cnt]
    if not tree.same(s,t):
        ans += w
        tree.union(s,t)
        group_num -= 1
    edge_cnt += 1

print(ans)




