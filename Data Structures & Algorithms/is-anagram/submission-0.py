class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_characters = sorted([s[i] for i in range(len(s))])
        t_characters = sorted([t[i] for i in range(len(t))])
        return s_characters == t_characters
        