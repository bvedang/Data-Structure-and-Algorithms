#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        dp ={}
        def helper(ind, N):
            if ind == 0:  return N*price[0]
            if (ind,N) in dp: return dp[(ind,N)]
            nottake = 0 + helper(ind-1,N)
            take = float("-inf")
            rodlength = ind+1
            if rodlength <= N:
                take = price[ind]+helper(ind,N-rodlength)
            dp[(ind,N)] = max(take,nottake)
            return dp[(ind,N)]
        return helper(n-1, n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends