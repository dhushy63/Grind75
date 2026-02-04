class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen_numbers:
                return [seen_numbers[diff], i]
            seen_numbers[num] = i