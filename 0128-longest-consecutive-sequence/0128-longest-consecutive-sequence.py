class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        final = 0
        for num in nums:
            
            if num-1 not in nums:
                length = 0
                while num + length in nums:
                    length += 1
                final = max(length, final)
        return final