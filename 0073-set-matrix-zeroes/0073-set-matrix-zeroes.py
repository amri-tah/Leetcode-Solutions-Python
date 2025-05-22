class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        updated = [0]*n
        affected = set()
        for row in range(m):
            for col in range(n):
                if matrix[row][col]==0: affected.add((row, col))
        for row, col in affected:
            matrix[row]=updated
            for i in range(m):
                matrix[i][col]=0

        