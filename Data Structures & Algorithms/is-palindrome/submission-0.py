class Solution:
    def flip_word(self, s:str) -> str:
        flipped = ''
        for i in range(len(s)):
            flipped += s[-1 - (i)]
        return flipped

    def isPalindrome(self, s: str) -> bool:
        text = s.replace(" ", "").lower()
        text_ascii=''
        for i in range(len(text)):
            if text[i].isalnum():
                text_ascii += text[i] 
        return self.flip_word(text_ascii) == text_ascii