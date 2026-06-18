class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1check, s2check = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1check[ord(s1[i]) - ord('a')] += 1
            s2check[ord(s2[i]) - ord('a')] += 1

        matches=0
        for i in range(26):
            matches += (1 if s1check[i] == s2check[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2check[index] += 1

            if s1check[index] == s2check[index]:
                matches += 1
            elif s1check[index] + 1 == s2check[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2check[index] -= 1
            
            if s1check[index] == s2check[index]:
                matches += 1

            elif s1check[index] - 1 == s2check[index]:
                matches -= 1

            l += 1
        return matches == 26