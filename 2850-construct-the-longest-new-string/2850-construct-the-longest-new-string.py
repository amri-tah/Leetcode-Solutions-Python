class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # x = "AA"
        # y = "BB"
        # z = "AB"

        dp = [[[[-1]*5 for _ in range(z+1)] for _ in range(y+1)] for _ in range(x+1)]

        def find(x, y, z, last):
            if dp[x][y][z][last+1] != -1: return dp[x][y][z][last+1]

            ans = 0
            if last == -1:
                if x: ans = max(ans, 2 + find(x-1, y, z, 1))  # AA
                if y: ans = max(ans, 2 + find(x, y-1, z, 2))  # BB
                if z: ans = max(ans, 2 + find(x, y, z-1, 3))  # AB
            else:
                if last == 1:  # AA
                    if y: ans = max(ans, 2 + find(x, y-1, z, 2))  
                elif last == 2:  # BB
                    if x: ans = max(ans, 2 + find(x-1, y, z, 1))  
                    if z: ans = max(ans, 2 + find(x, y, z-1, 3))
                else:  # AB
                    if x: ans = max(ans, 2 + find(x-1, y, z, 1)) 
                    if z: ans = max(ans, 2 + find(x, y, z-1, 3)) 
            dp[x][y][z][last+1] = ans
            return ans

        return find(x, y, z, -1)