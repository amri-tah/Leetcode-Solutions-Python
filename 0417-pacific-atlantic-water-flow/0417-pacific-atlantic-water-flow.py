class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        result = []
        m, n = len(heights), len(heights[0])
        def dfs(x, y, ocean, prevVal):
            if (x,y) in ocean or x<0 or x==m or y<0 or y==n or heights[x][y]<prevVal: return 
            ocean.add((x,y))
            dfs(x+1, y, ocean, heights[x][y])
            dfs(x-1, y, ocean, heights[x][y])
            dfs(x, y+1, ocean, heights[x][y])
            dfs(x, y-1, ocean, heights[x][y])

        for col in range(n):
            dfs(0, col, pacific, heights[0][col])
            dfs(m-1, col, atlantic, heights[m-1][col])
        for row in range(m):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, n-1, atlantic, heights[row][n-1])
        
        for r in range(m):
            for c in range(n):
                if (r,c) in pacific and (r,c) in atlantic:result.append([r, c])
        return result