class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        elif numRows == 1: return [[1]]
        output = [[1]]

        for i in range(1, numRows):
            row = [1] * (i + 1)
            prevRow = output[-1]
            for j in range(1, i):
                row[j] = prevRow[j-1] + prevRow[j]
            output.append(row)
        return output