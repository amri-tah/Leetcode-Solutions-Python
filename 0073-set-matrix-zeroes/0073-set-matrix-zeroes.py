class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_i, cols_i = [], []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    rows_i.append(row)
                    cols_i.append(col)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row in rows_i or col in cols_i:
                    matrix[row][col] = 0
