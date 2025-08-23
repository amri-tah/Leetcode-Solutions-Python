class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        net = [gas[i] - cost[i] for i in range(n)]
        if sum(net) < 0: return -1
        tank = 0
        start = 0
        for i in range(n):
            tank += net[i]
            if tank<0:
                tank=0
                start=i + 1
        return start