#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        dp = {}
        def helper(i,j):
            if i == j: return 0
            if (i,j) in dp: return dp[(i,j)]
            mini = float("inf")
            for k in range(i,j):
                steps = arr[i-1]*arr[k]*arr[j] + helper(i,k)+helper(k+1,j)
                mini = min(steps,mini)
                dp[(i,j)] = mini
            return dp[(i,j)]
        return helper(1,N-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends