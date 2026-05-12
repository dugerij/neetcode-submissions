class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        for i in range(len(s)):
            noted_characters =[]
            for j in range(len(s)):
                if (j>=i):
                    if s[j] not in noted_characters:
                        noted_characters.append(s[j])
                    else:
                        break
                if len(noted_characters) > longest:
                    longest = len(noted_characters)
        
        return longest
