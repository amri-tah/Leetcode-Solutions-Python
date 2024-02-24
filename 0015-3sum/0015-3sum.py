class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # Sort 
        nums.sort()
        
        # Keep one element for i fixed and 2 sum on the following values 
        for i in range(len(nums)-1):
            if i>0 and nums[i]==nums[i-1]:
                 continue
            elif nums[i]>0:
                break
                
            # perform 2 sum on the remaining using pointers
            left = i+1
            right = len(nums)-1
            while left<right:
                threeSum = nums[i]+nums[left]+nums[right]
                if threeSum>0:
                    right-=1
                elif threeSum<0:
                    left+=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return result