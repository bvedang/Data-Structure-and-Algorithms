class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.lists = nums
        heapq.heapify(self.lists)
        while len(self.lists) > self.k:
            heapq.heappop(self.lists)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.lists,val)
        while len(self.lists) > self.k:
            heapq.heappop(self.lists)
        return self.lists[0]
        
            

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)