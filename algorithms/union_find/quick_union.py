class QuickUnion:
    def __init__(self, N):
        self.id = list(range(0, N))

    def connected(self, p, q):
        return self.find_root(p) == self.find_root(q)

    def union(self, p, q):
        if not self.connected(p, q):
            self.id[q] = self.find_root(p)

    def find_root(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p
