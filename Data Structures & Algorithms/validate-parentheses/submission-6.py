class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs={
            '(':')',
            '[':']',
            '{':'}'
        }
        stack=[]

        for char in s:
            if char in bracket_pairs:
                stack.append(char)
            
            else:
                if not stack:
                    return False

                top = stack.pop()
                
                if bracket_pairs[top] != char:
                    return False

        return len(stack) == 0