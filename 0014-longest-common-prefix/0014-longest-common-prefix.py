class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i, min_len = 0, min(len(s) for s in strs)
        while i < min_len:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        return strs[0][:i]
