class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0]*(len(arr)+1)
        for i in range(len(arr)):
            xors[i+1]=xors[i]^arr[i]
        return [xors[right+1]^xors[left] for left, right in queries]