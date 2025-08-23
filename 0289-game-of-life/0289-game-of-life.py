class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # ded => -2
        # alive => +2
        m, n = len(board), len(board[0])
        def count_live(r, c):
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), 
                    (1, 1), (1, -1), (-1, 1), (-1, -1)]
            count = 0
            for x, y in dirs:
                nx, ny = x+r, y+c
                if 0<=nx<m and 0<=ny<n:
                    if board[nx][ny]==1 or board[nx][ny]==-1: count+=1
            return count

        for row in range(m):
            for col in range(n):
                count = count_live(row, col)
                if board[row][col]==1:
                    if count<2 or count>3: board[row][col]=-1
                    elif count==2 or count==3: board[row][col]=1
                else:
                    if count==3: board[row][col]=2
    
        for row in range(m):
            for col in range(n):
                if board[row][col] > 0: board[row][col] = 1
                else: board[row][col]=0