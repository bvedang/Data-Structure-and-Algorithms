class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_heap = []
        for point in points:
            distance = ((0-point[0])**2) + ((0-point[1])**2)
            point.insert(0,(-1)*distance)
            if len(distance_heap) < k :
                heapq.heappush(distance_heap,point)
            else:
                top = distance_heap[0][0]
                if distance < top*(-1):
                    heapq.heappop(distance_heap)
                    heapq.heappush(distance_heap,point)
        for points in distance_heap:
            points.pop(0)
        return distance_heap
        