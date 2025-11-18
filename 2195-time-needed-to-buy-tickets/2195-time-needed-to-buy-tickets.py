class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = 0
        pos = k
        queue = deque(tickets)
        while True:
            t += 1
            curr = queue.popleft()
            curr -= 1
            if curr > 0: queue.append(curr)
            if pos == 0:
                if curr == 0: return t
                pos = len(queue) - 1   
            else: pos -= 1