class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = {}
        def dp(i, j):
            if (i, j) in mem: return mem[(i, j)]
            if i==0: return j # if word1 empty, then need to insert j chars from word2
            if j==0: return i # if word2 empty, then need to delete j chars from word1
            if word1[i-1]==word2[j-1]: res = dp(i-1, j-1) # if match then move both ptrs
            else: 
                res = 1+min(
                    dp(i-1, j), # delete
                    dp(i, j-1), # insert
                    dp(i-1, j-1) # replace
                )
            mem[(i, j)]=res
            return res
        return dp(len(word1), len(word2))
