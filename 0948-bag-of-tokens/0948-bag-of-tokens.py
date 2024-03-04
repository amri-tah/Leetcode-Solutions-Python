class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        maxScore = 0
        tokens.sort()
        left, right = 0, len(tokens)-1
        while left<=right:
            # If enough power to get token - Face Up
            if tokens[left]<=power:
                score += 1
                power -= tokens[left]
                left += 1
                maxScore = max(maxScore, score)
                
            # If enough score to trade for token - Face Down
            elif score>0:
                score -= 1
                power += tokens[right]
                right -= 1
            
            else:
                break
        return maxScore
            