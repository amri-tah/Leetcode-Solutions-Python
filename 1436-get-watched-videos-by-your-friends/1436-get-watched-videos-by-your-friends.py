class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        adj = {i: friend for i, friend in enumerate(friends)}
        visited = set([id])
        queue = deque([id])
        for l in range(level):
            for _ in range(len(queue)):
                curr = queue.popleft()
                for neigh in friends[curr]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)

        count = defaultdict(int)
        for friend in queue:
            for video in watchedVideos[friend]:
                count[video] += 1
        result = sorted(count.keys(), key=lambda x: (count[x], x))
        return result
            
