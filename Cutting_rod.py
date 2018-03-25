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
