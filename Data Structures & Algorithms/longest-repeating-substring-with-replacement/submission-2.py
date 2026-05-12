class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        record = {}
        longest_count = 0
        start = 0
        answer = 0

        for i in range(len(s)):
            if s[i] in record:
                record[s[i]] += 1
            else:
                record[s[i]] = 1
            
            if record[s[i]] > longest_count:
                longest_count = record[s[i]]
            
            while (i-start+1) - longest_count > k:
                record[s[start]] -= 1
                start+=1
            
            longest_consecutive = i - start + 1
            if longest_consecutive > answer:
                answer = longest_consecutive

        return answer