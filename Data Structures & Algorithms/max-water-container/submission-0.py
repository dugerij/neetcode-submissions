class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i != j:
                    amount = (j - i) * min(heights[i], heights[j])
                    if amount > max_amount:
                        max_amount = amount
        return max_amount