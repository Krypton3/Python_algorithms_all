import math

# finding maximum value in a given range using segment tree.
# similarly one could find minimum and sum of the given range


class SegmentTree:
    def __init__(self, Array):
        self.N = len(Array)
        self.st = [0] * (4*self.N)
        self.build(1, 0, self.N-1)

    def build(self, indx, l, r):
        if l == r:
            self.st[indx] = Array[l]
        else:
            mid = (l+r) // 2
            self.build(indx * 2, l, mid)
            self.build(indx * 2 + 1, mid+1, r)
            self.st[indx] = max(self.st[indx * 2], self.st[indx * 2 + 1])

    def query(self, indx, l, r, a, b):
        if r < a or l > b:
            return -math.inf
        if l >= a and r <= b:
            return self.st[indx]
        mid = (l + r) // 2
        m1 = self.query(indx * 2, l, mid, a, b)
        m2 = self.query(indx * 2 + 1, mid + 1, r, a, b)
        return max(m1, m2)

    def update(self, indx, l, r, a, b, val):
        if r < a or l > b:
            return True
        if l == r:
            self.st[indx] = val
            return True
        mid = (l + r) // 2
        self.update(indx * 2, l, mid, a, b, val)
        self.update(indx * 2 + 1, mid + 1, r, a, b, val)
        self.st[indx] = max(self.st[indx * 2], self.st[indx * 2 + 1])
        return True


if __name__ == '__main__':
    Array = [1, 2, -4, 7, 3, -5, 6, 11, -20, 9, 14, 15, 5, 2, -8]
    N = 15
    sgt = SegmentTree(Array)
    print(sgt.query(1, 0, N-1, 4, 6))
    print(sgt.query(1, 0, N-1, 7, 11))
    print(sgt.query(1, 0, N-1, 7, 12))
    print(sgt.update(1, 0, N-1, 1, 3, 111))
    print(sgt.query(1, 0, N-1, 1, 15))
