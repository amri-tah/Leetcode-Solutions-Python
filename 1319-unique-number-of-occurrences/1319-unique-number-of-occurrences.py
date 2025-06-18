class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        occset = set()
        i = 0
        while i<len(arr):
            fixed = arr[i]
            count = 0
            while i<len(arr) and arr[i]==fixed:
                i+=1
                count+=1
            if count in occset: return False
            occset.add(count)
        return True
