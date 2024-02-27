class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Pointers for finding the mid row
        top, bottom = 0, len(matrix)-1
        
        while top<=bottom:
            mid = (top+bottom)//2
            
            # If first element is greater than target, it will be present in that row
            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                break
            # If last element of the mid row is greater than target, it might be in the above row
            elif matrix[mid][-1]>target:
                bottom = mid-1
            
            else:
                top = mid+1
            
        # Check if the element is in that row
        left, right = 0, len(matrix[mid]) - 1
        while left<=right:
            mid_col = (left+right)//2
            if target==matrix[mid][mid_col]: return True
            elif matrix[mid][mid_col]>target: right = mid_col - 1
            else: left = mid_col + 1
        
        # If not found
        return False
    
                
                
                
                
                    
                
                
        