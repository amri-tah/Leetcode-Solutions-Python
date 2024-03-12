class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result=""
        for i in order:
            count=s.count(i)
            if i in set(s):
                result+=(i*count)
        for i in s:
            count=s.count(i)
            if i not in set(result):
                result+=(i*count)
        return result