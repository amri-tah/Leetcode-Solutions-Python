class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        sandwiches.reverse()
        count = 0
        while len(queue)>count:
            if sandwiches[-1]==queue[0]: 
                queue.popleft()
                sandwiches.pop()
                count=0
            else:
                queue.append(queue.popleft())
                count+=1
        return count