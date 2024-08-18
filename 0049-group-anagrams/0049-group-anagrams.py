class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in hash: hash[s_sorted].append(s)
            else: hash[s_sorted] = [s]
        return list(hash.values())

        