class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        result = left = right = 0
        for j in range(len(nums)):
            count[nums[j]]+=1
            
            while len(count)>k:
                count[nums[left]]-=1
                if count[nums[left]] == 0:
                    count.pop(nums[left])
                left+=1
                right = left
            
            while count[nums[left]]>1:
                count[nums[left]]-=1
                left+=1
            
            if len(count)==k:
                result += left-right+1
        return result
            