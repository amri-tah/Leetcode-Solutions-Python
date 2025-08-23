class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_st, map_ts = {}, {}
        for s_char, t_char in zip(s, t):
            if (s_char in map_st and map_st[s_char] != t_char) or \
               (t_char in map_ts and map_ts[t_char] != s_char):
                return False
            map_st[s_char] = t_char
            map_ts[t_char] = s_char

        return True
