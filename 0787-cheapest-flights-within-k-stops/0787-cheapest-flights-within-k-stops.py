class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("INF")]*n
        prices[src] = 0
        
        for i in range(k+1):
            temp = prices.copy()
            for s,d,cost in flights:
                if prices[s] == float("INF"):
                    continue
                if prices[s] + cost < temp[d]:
                    temp[d] = prices[s] + cost
            prices = temp
        
        if prices[dst] == float("INF"):
            return -1
        return prices[dst]