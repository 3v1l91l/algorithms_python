class QuickFind:
    def __init__(self, N):
        self.id = list(range(0, N))

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        if self.id[p] != self.id[q]:
            pid = self.id[p]
            qid = self.id[q]
            for i in range(0,len(self.id)):
                if self.id[i] == pid:
                    self.id[i] = qid
