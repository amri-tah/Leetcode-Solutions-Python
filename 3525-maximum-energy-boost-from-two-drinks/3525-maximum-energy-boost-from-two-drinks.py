class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        # Max energy boost by drinking energy drink i for hour j
        n = len(energyDrinkA)
        dpA, dpB = [0]*n, [0]*n

        dpA[0], dpB[0] = energyDrinkA[0], energyDrinkB[0]
        for i in range(1, n):
            # Max energy boost if i choose to stay on Energy A or change to EnergyB
            dpA[i] = max(dpA[i-1]+energyDrinkA[i], dpB[i-1]) 
            # Max energy boost if i choose to stay on Energy B or change to EnergyA
            dpB[i] = max(dpB[i-1]+energyDrinkB[i], dpA[i-1])
        return max(dpA[-1], dpB[-1])