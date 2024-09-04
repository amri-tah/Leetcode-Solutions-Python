class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Iterate thru the commands
        # Update x and y
        # If obstacle encountered: move on
        direction = "N"
        x, y, dist = 0, 0, 0
        obstacles = set(map(tuple, obstacles))
        directions = {"N": (0, 1),"E": (1, 0), "S": (0, -1), "W": (-1, 0)}
        change_dir = {"E": ["N", "S"], "W": ["S","N"], "N": ["W", "E"], "S":["E", "W"]} # curr dir: [left, right]
        
        for command in commands:
            if command in [-1, -2]: direction = change_dir[direction][command]
            else:
                for _ in range(command):
                    nx, ny = x + directions[direction][0], y+directions[direction][1]
                    if (nx, ny) not in obstacles:
                        x, y = nx, ny
                        dist = max(dist, x**2 + y**2)
                    else: break
        return dist