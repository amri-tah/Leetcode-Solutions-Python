class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        output = []
        left, right = 0, len(products) - 1
        
        for i, c in enumerate(searchWord):
            while left <= right and (len(products[left]) <= i or products[left][i] != c):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != c):
                right -= 1
            
            result = []
            for j in range(min(3, right - left + 1)):
                result.append(products[left + j])
            output.append(result)
        
        return output
