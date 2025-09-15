class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        count = 0
        brokenLetters = set(brokenLetters)
        for s in text:
            s = set(s)
            if len(s.intersection(brokenLetters))!=0: continue
            else: count+=1
        return count