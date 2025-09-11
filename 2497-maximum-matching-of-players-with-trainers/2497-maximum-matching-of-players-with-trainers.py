class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # player[i]<=trainer[j]
        players.sort()
        trainers.sort()
        i, j = 0, 0
        count = 0
        while i<len(players) and j<len(trainers):
            if players[i]<=trainers[j]:
                i+=1
                j+=1
                count +=1
            else: j+=1
        return count