class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] =1
        
        bucket = [[] for i in range(len(nums)+1)]
        for key, val in freq.items():
            bucket[val].append(key)
        res =[]
        for i in range(len(nums),0,-1):
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res
                
            