#User function Template for python3
class Solution:
	def minOperations(self, s1, s2):
		def helper(s1,s2):
		    dp ={}
		    res = 0
		    for ind2 in range(len(s2)+1):dp[ind2] = 0
		    for ind1 in range(1,len(s1)+1):
		        temp = {ind2:0 for ind2 in range(len(s2)+1)}
		        for ind2 in range(1,len(s2)+1):
		            if s1[ind1-1] == s2[ind2-1]:
		                temp[ind2] = 1 + dp[ind2-1]
		            else:
		                temp[ind2] = 0+max(dp[ind2],temp[ind2-1])
		        dp = temp
		    return dp[len(s2)]
		ans = helper(s1,s2)
		return (len(s1) - ans) + (len(s2)-ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends