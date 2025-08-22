class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(pick, i, partial):
            if pick==4:
                if i==len(s): res.append(partial)
                return
            for j in range(1, 4):
                if i+j > len(s): break
                num = s[i:i+j]
                if len(num) > 1 and num[0] == "0": continue
                if int(num) <= 255:
                    backtrack(pick + 1, i + j, partial + num + ("." if pick < 3 else ""))
        backtrack(0, 0, "")
        return res