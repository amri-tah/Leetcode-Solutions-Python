class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        pattern_to_word = {}
        word_to_pattern = {}
        
        for pat, word in zip(pattern, words):
            # Pattern to word mapping
            if pat in pattern_to_word:
                if pattern_to_word[pat] != word:
                    return False
            else:
                pattern_to_word[pat] = word
            
            # Word to pattern mapping
            if word in word_to_pattern:
                if word_to_pattern[word] != pat:
                    return False
            else:
                word_to_pattern[word] = pat
        
        return True
