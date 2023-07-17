class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] +=1
            else:
                counter[n] = 1
        n = len(nums)
        for key, value in counter.items():
            if value > n/2:
                return key
            else:
                continue
                