class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter ={}
        for n in nums:
            if n in counter:
                counter[n] +=1
            else:
                counter[n] =1
        
        n = len(nums)
        res = []
        for key, value in counter.items():
            if value > n/3:
                res.append(key)
            else:
                continue
        return res