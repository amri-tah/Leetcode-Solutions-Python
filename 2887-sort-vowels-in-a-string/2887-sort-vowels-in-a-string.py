class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        vow = [st for st in s if st in vowels]
        vow.sort()
        s = list(s)
        j =0
        for i in range(len(s)):
            if s[i] in vowels: 
                s[i]=vow[j]
                j+=1
        return "".join(s)