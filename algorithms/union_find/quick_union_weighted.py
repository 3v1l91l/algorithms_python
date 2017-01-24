class QuickUnionWeighted:
    def __init__(self, N):
        self.id = list(range(0, N))
        self.treeSize = [1] * N

    def connected(self, p, q):
        return self.find_root(p) == self.find_root(q)

    def union(self, p, q):
        if not self.connected(p, q):
            if self.treeSize[p] > self.treeSize[q]:
                self.id[self.find_root(q)] = self.find_root(p)
                self.treeSize[p] += self.treeSize[q]
            else:
                self.id[self.find_root(p)] = self.find_root(q)
                self.treeSize[q] += self.treeSize[p]

    def find_root(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p
