class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        n = len(nums)
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] =1
        res =[]
        bucket = [[] for i in range(n+1)]
        for key, val in freq.items():
            bucket[val].append(key)
        
        for i in range(n,0,-1):
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res
        