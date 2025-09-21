class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        queue = deque([nums1])
        count = 0
        visited = set(tuple(nums1))
        while queue:
            for _ in range(len(queue)): # level wise exploration
                newnums = queue.popleft()
                if newnums==nums2: return count
                for l in range(len(newnums)):
                    for r in range(l, len(newnums)): # all possible [l,r]
                        cut = newnums[l:r+1]
                        rem = newnums[:l]+newnums[r+1:]
                        for i in range(len(rem)+1): # all possible indexes i in remaining array
                            final = rem[:i]+cut+rem[i:]
                            t = tuple(final)
                            if t not in visited:
                                visited.add(t)
                                queue.append(final)
            count += 1 
        return -1