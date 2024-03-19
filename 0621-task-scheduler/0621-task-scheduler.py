class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        table = [0]*26
        for task in tasks:
            table[ord(task)-ord('A')]+=1
        table.sort()
        maxfreq = table[-1]-1
        idle = maxfreq*n
        for i in range(24, -1, -1):
            idle -= min(maxfreq, table[i])
        if idle>0:
            return idle+len(tasks)
        return len(tasks)