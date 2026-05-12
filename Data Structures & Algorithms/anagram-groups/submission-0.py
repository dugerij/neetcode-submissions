class Solution:
    def checkAnagram(self, s: str, t: str) -> bool:
        s_characters = sorted([s[i] for i in range(len(s))])
        t_characters = sorted([t[i] for i in range(len(t))])
        return s_characters == t_characters

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = []
        for word in strs:
            no_anagram = True
            if len(anagram_groups) != 0:
                for group_idx in range(len(anagram_groups)):
                    word_in = anagram_groups[group_idx][0]
                    if self.checkAnagram(word, word_in):
                        anagram_groups[group_idx].append(word)
                        no_anagram =False
                
            if no_anagram:
                anagram_groups.append([word])
        return anagram_groups           