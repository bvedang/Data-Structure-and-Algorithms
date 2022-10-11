class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) ==1:
            return nums[0]
        heapq.heapify(nums)
        kth = len(nums) - k
        while kth:
            heapq.heappop(nums)
            kth -=1
        return nums[0]