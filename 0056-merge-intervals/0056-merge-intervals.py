class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newInt = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not newInt or newInt[-1][1]<interval[0]: newInt.append(interval)
            else: newInt[-1][1] = max(newInt[-1][1], interval[1])
        return newInt