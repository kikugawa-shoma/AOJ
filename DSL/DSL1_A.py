n,q = map(int,input().split())
commands = [0]*q
args = [[0,0] for _ in range(q)]
for i in range(q):
    tmp = list(map(int,input().split()))
    commands[i] = tmp[0]
    args[i] = tmp[1:3]

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

tree = UnionFind(n)

for i in range(q):
    if commands[i] == 0:
        tree.union(args[i][0],args[i][1])
    else:
        if tree.same(args[i][0],args[i][1]):
            print(1)
        else:
            print(0)


