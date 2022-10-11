class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 0:
            if len(stones) == 1:
                return ((-1)*stones[0])
            largest = heapq.heappop(stones) * (-1)
            second_largest = heapq.heappop(stones) * (-1)
            if largest - second_largest > 0:
                heapq.heappush(stones, (-1)*(largest - second_largest))
        return 0