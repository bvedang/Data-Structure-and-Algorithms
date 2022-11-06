#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        dp = {}
        for weight in range(W+1):
            dp[(0,weight)] = val[0]*(weight//wt[0])
        
        for ind in range(1,N):
            for weight in range(W+1):
                nottake = dp[(ind-1, weight)]
                take = float("-inf")
                if weight >= wt[ind]:
                    take = val[ind] + dp[(ind,weight-wt[ind])]
                dp[(ind,weight)] = max(take, nottake)
        return dp[(N-1, W)]
        # def helper(ind, weight):
        #     if ind == 0:
        #         return val[0]*(weight//wt[0])
        #     if (ind, weight) in dp: return dp[(ind,weight)]
        #     nottake = helper(ind-1, weight)
        #     take = float("-inf")
        #     if weight >= wt[ind]:
        #         take = val[ind] + helper(ind,weight-wt[ind])
        #     dp[(ind,weight)] = max(nottake, take)
        #     return dp[(ind,weight)]
        # return helper(N-1, W)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends