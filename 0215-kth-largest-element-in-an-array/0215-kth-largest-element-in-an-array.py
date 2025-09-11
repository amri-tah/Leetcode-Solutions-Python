class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        while k>1:
            heapq.heappop(nums)
            k-=1
        return -heapq.heappop(nums)