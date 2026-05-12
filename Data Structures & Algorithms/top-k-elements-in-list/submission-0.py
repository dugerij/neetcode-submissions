class Solution:
    def check_duplicates(self, number: int, nums: List[int]) -> int:
        duplicate_count = 0
        for i in nums:
            if i == number:
                duplicate_count += 1
        return duplicate_count
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        duplicate_record ={}
        for i in set(nums):
            duplicate_record[i] = self.check_duplicates(i, nums)

        sorted_keys = sorted(duplicate_record, key=lambda x: duplicate_record[x], reverse=True)

        return sorted_keys[:k]
