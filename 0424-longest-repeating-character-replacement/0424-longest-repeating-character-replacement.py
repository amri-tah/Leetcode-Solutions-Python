class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res, left = 0, 0
        for right in range(len(s)):
            count[s[right]]+=1
            while right-left+1-max(count.values())>k:
                count[s[left]]-=1
                left+=1
            res = max(res, right-left+1)
        return res