class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            left, right = 0, len(matrix[0])-1
            while left<right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left+=1
                right-=1