class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        mintime = tasks[0][0]+tasks[0][1]
        for t in tasks:
            mintime=min(mintime, t[0]+t[1])
        return mintime