class MedianFinder:

    def __init__(self):
        # self.nums=[]
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # self.nums.append(num)
        # self.nums.sort()
        heapq.heappush(self.small, -num)

        # small heap value larger than large heap
        if self.small and self.large and -self.small[0]>self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # unbalanced
        if len(self.small)>len(self.large)+1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.large)>len(self.small)+1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        # mid = len(self.nums)//2
        # if len(self.nums)%2!=0: return self.nums[mid]
        # else: return (self.nums[mid]+self.nums[mid-1])/2

        if len(self.small)>len(self.large):
            return -self.small[0]
        if len(self.large)>len(self.small):
            return self.large[0]
        else: 
            return (-self.small[0]+self.large[0])/2
        
# brute force
# use list -> addNum then simply push and sort (O(nlogn))
        #  -> check if the list is even then mid mean else mid value

# optimal 
# 2 heaps 1 small (maxheap) 1 large (minheap)
# balanced the size diff approx 1 
# all values (maxvalues) in the small heap <= large



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()