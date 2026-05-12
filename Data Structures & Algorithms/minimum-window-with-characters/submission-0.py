from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer =""
        t_count = Counter(t)

        for i in range(len(t), len(s)+1):
            for j in range(len(s)):
                if (i - j) >= len(t):
                    sub = s[j:i]
                    sub_count = Counter(sub)

                    if (
                        (answer == "" or len(sub) < len(answer))
                        and sub_count >= t_count
                    ):
                        answer = sub       
        return answer