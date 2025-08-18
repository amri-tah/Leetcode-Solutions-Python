class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        block = 2*k+1
        return ceil(n/block)*ceil(m/block)