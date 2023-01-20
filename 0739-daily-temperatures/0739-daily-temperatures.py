class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        res =[0 for i in range(len(temperatures))]
        for index, val in enumerate(temperatures):
            if index == 0:
                stack.append((index,val))
            while stack and val > stack[-1][1]:
                residx,stackval = stack.pop()
                res[residx] = index - residx
            stack.append((index,val))
        
        return res