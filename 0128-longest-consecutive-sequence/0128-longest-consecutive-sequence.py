class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seq = 0
        for num in nums:
            if (num -1) not in nums:
                length = 1
                while (num + length) in nums:
                    length +=1
                seq = max(seq, length)
        return seq