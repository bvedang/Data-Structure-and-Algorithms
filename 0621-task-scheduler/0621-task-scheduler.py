class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = 1+ count.get(task,0)
        heap = [-i for i in count.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt < 0:
                    q.append((cnt, time+n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time
            