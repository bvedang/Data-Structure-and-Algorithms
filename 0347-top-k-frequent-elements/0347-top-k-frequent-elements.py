class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        buckets = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i in count:
                count[i] +=1
            else:
                count[i] = 1
        for key,val in count.items():
            buckets[val].append(key)
        res = []
        print(buckets)
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
                