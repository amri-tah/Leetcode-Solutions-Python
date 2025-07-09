class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        arrow = 1
        points.sort(key=lambda x: x[1])
        last = points[0]
        for i in range(1, len(points)):
            if last[1]<points[i][0]:
                arrow+=1
                last = points[i]
        return arrow