#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        cache = [[0]*(W+1) for i in range(n)]
        for i in range(wt[0],W+1):
                cache[0][i] = val[0]
        for i in range(1,n):
            for capacity in range(W+1):
                notpick = cache[i-1][capacity]
                pick = float("-inf")
                if capacity >= wt[i]:
                    pick = val[i] + cache[i-1][capacity-wt[i]]
                cache[i][capacity] = max(pick,notpick)
        return cache[n-1][W]
        # def helper(i, capacity):
        #     if i == 0:
        #         if (capacity >= wt[0]):
        #             return val[0]
        #         return 0
        #     if cache[i][capacity] != -1:
        #         return cache[i][capacity]
        #     notpick = helper(i-1,capacity)
        #     pick = float("-inf")
        #     if capacity >= wt[i]:
        #         pick = val[i]+helper(i-1, capacity-wt[i])
        #     cache[i][capacity] = max(pick,notpick)
        #     return cache[i][capacity]
        # return helper(n-1, W)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends