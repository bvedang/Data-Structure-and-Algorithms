class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        if 0 in counter:
            for i in range(counter[0]):
                nums[i] = 0
        if 1 in counter:
            if 0 in counter:
                for i in range(counter[0],counter[0]+counter[1]):
                    nums[i] = 1
            else:
                for i in range(counter[1]):
                    nums[i] = 1
        if 2 in counter:
            if 0 in counter and not 1 in counter:
                for i in range(counter[0], len(nums)):
                    nums[i] = 2
            elif 0 not in counter and 1 in counter:
                for i in range(counter[1], len(nums)):
                    nums[i] = 2
            elif 0 in counter and 1 in counter:
                for i in range(counter[0]+counter[1], len(nums)):
                    nums[i] = 2
            else:
                for i in range(len(nums)):
                    nums[i] = 2
            