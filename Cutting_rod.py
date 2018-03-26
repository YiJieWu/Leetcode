# The brutal force solution

class Solution:
    """
    @param prices: the prices
    @param n: the length of rod
    @return: the max value
    """
    def cutting(self, prices, n):
        # Write your code here
        res=0
        for top in range(1,n+1):
            res=max(res,prices[top-1]+self.cutting(prices,n-top))
        return res




# try to cache the res

class Solution:
    """
    @param prices: the prices
    @param n: the length of rod
    @return: the max value
    """
    def helper(self,prices,n,dp):
        res=0
        for top in range(1,n+1):
            if n-top not in dp:
                dp[n-top]=self.helper(prices,n-top,dp)
            res=max(res,prices[top-1]+dp[n-top])
        return res
    def cutting(self, prices, n):
        # Write your code here
        
        dp=[0]*(n+1)
        return self.helper(prices,n,dp)
