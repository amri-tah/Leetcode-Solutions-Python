class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []     
        prev = 0   
        
        for log in logs:
            fid, typ, ts = log.split(":")
            fid, ts = int(fid), int(ts)
            if typ == "start":
                if stack: res[stack[-1]] += ts - prev
                stack.append(fid)
                prev = ts
            else:  
                res[stack.pop()] += ts - prev + 1
                prev = ts + 1
        return res