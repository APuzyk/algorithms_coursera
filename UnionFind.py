class UnionFind:
    a = []

    def __init__(self, n):
        self.a = [[i, 0] for i in range(n)]

    # Need to add compresion to speed it up
    def find(self, v):
        if self.a[v][0] == v:
            return v
        while self.a[v][0] != v:
            v = self.a[v][0]
        if v != self.a[v][0]:
            raise RuntimeError
        return v

    def union(self, v, u):
        # get V's parent
        # implment size for speed up
        p_v = self.find(v)
        p_u = self.find(u)
        if self.a[p_u][1] >= self.a[p_v][1]:
            self.a[p_v][0] = p_u
            self.a[p_v][1] += self.a[p_u][1]
        else:
            self.a[p_u][0] = p_v
            self.a[p_u][1] += self.a[p_v][1]

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def num_clusters(self):
        return len(list(set([self.find(i) for i in range(len(self.a))])))

    def clusters(self):
        return list(set([self.find(i) for i in range(len(self.a))]))
