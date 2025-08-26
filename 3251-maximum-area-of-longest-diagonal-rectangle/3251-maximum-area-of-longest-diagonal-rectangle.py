class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxdiag = 0 
        maxarea = 0
        for l, b in dimensions:
            diag = l*l + b*b
            area = l * b
            
            if diag > maxdiag:
                maxdiag = diag
                maxarea = area
            elif diag == maxdiag: maxarea = max(maxarea, area)
        
        return maxarea