class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        right = 0
        output = ""
        for right in range(len(word)):
            if word[right]==ch:
                temp = word[right+1:]
                while right>=0:
                    output+=word[right]
                    right-=1
                output+=temp
                return output
            right+=1
        return word
            