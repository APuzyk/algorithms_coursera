class UnionFind:
    a = []

    def __init__(self, n):
        self.a = [i for i in range(n)]

    # forget weights for the time being
    def find(self, v):
        if self.a[v] == v:
            return v
        while self.a[v] != v:
            v = self.a[v]
        if v != self.a[v]:
            raise RuntimeError
        return v

    def union(self, v, u):
        # get V's parent
        # implment size for speed up
        p = self.find(v)
        self.a[p] = u

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def num_clusters(self):
        return len(list(set([self.find(i) for i in range(len(self.a))])))

    def clusters(self):
        return list(set([self.find(i) for i in range(len(self.a))]))
