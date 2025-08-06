class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        size = 4 * n
        seg = [-1] * size

        def build(i, l, r):
            if l == r:
                seg[i] = baskets[l]
                return
            mid = (l + r) // 2
            build(2 * i + 1, l, mid)
            build(2 * i + 2, mid + 1, r)
            seg[i] = max(seg[2 * i + 1], seg[2 * i + 2])

        def query(i, l, r, val):
            if seg[i] < val: return False  # No valid basket in this range
            if l == r:
                seg[i] = -1  # Mark as used
                return True
            mid = (l + r) // 2
            placed = False
            if seg[2 * i + 1] >= val: placed = query(2 * i + 1, l, mid, val)
            else: placed = query(2 * i + 2, mid + 1, r, val)
            seg[i] = max(seg[2 * i + 1], seg[2 * i + 2])
            return placed

        build(0, 0, n - 1)
        unplaced = 0
        for fruit in fruits:
            if not query(0, 0, n - 1, fruit):
                unplaced += 1
        return unplaced