class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            d[sorted_word].append(word)
        res = []
        for k, v in d.items():
            res.append(v)

        return res