class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxel, count, i, maxwin = max(nums), 0, 0, 0
        for j in range(len(nums)):
            # Increment max element in window 
            # count by 1 when max element encountered
            if nums[j]==maxel: maxwin+=1
            
            # Shrink the window till maxwin = k
            while maxwin==k:
                if nums[i]==maxel: maxwin-=1
                i+=1
            count+=i
        return count