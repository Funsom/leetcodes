class UnionFind(object):
    def __init__(self,n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def union(self,p,q) -> None:
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.count -= 1
    def find(self,x) -> int:
        while self.parent[x] != x :
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def connected(self,p,q) -> bool:
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ

if __name__ == "__main__":
    uf = UnionFind(10)
    uf.union(0,1)
    uf.union(2,3)
    print(uf.connected(1,2))