class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(num1, num2) for num1, num2 in zip(nums1, nums2)]
        pairs.sort(key=lambda x: x[1], reverse=True)
        output, prefix = 0, 0
        heap = []
        for num1, num2 in pairs:
            prefix+=num1
            heapq.heappush(heap, num1)
            if len(heap)>k: 
                temp = heapq.heappop(heap)
                prefix-=temp
            if len(heap)==k: output = max(output, prefix*num2)
        return output