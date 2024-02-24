class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_i, cols_i = self.findZeroes(matrix)
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row in rows_i or col in cols_i:
                    matrix[row][col] = 0
        
    def findZeroes(self, matrix):
        rows, cols = [], []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    rows.append(row)
                    cols.append(col)
        return rows, cols