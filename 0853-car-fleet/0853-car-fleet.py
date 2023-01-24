class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:return 1
        n = len(position)
        pair = [(position[i], speed[i]) for i in range(n)]
        stack = []
        for pos, s in sorted(pair)[::-1]:
            stack.append((target - pos) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
                
            
        