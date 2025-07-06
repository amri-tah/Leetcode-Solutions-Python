class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque([])
        d = deque([])
        n = len(senate)
        for i, s in enumerate(senate):
            if s=="R": r.append(i)
            else: d.append(i)
        while r and d:
            rad = r.popleft()
            dire = d.popleft()
            if rad<dire: r.append(rad+n)
            else: d.append(dire+n)

        return "Radiant" if r else "Dire"