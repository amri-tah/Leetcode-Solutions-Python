class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOcc = defaultdict(int)
        for i, char in enumerate(s):
            lastOcc[char] = i
        
        output, size, end = [], 0, 0
        for i, char in enumerate(s):
            size+=1
            end = max(end, lastOcc[char])
            if i==end: 
                output.append(size)
                size = 0
        return output