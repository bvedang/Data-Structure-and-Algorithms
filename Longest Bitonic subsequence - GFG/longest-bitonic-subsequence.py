#User function Template for python3

class Solution:
	def LongestBitonicSequence(self, nums):
		n = len(nums)
		dp = [1]*(n)
		for i in range(n):
		    for prev in range(i):
		        if nums[i] > nums[prev] and dp[i]<dp[prev]+1:
		            dp[i] = 1+dp[prev]
		    
		res = 0            
		dp1 = [1]*n
		for i in range(n-1,-1,-1):
		    for prev in range(n-1,i,-1):
		        if nums[i] > nums[prev] and dp1[i]<dp1[prev]+1:
		            dp1[i] = 1+dp1[prev]
		    res = max(dp[i]+dp1[i]-1, res)
	
		return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.LongestBitonicSequence(nums)
		print(ans)
# } Driver Code Ends