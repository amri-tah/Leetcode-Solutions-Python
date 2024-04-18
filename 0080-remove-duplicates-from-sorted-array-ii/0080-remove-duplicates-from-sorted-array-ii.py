class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashtable = {}
        index = 0
        
        for num in nums:
            hashtable[num] = hashtable.get(num, 0)+1
            if hashtable[num]<=2:
                nums[index] = num
                index+=1
                
        return index
            
                