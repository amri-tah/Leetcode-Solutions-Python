class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        i = 0
        for letter in ransomNote:
            if letter in magazine:
                magazine.remove(letter)
                continue
            else:
                return False
        return True