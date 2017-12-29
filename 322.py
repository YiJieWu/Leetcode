class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        #I want to use dp[i] to denotes that for amout i, what's the fewest coin 
        dp=[sys.maxint]*(amount+1)
        dp[0]=0
        for amount in xrange(1,len(dp)):
            for value_index in xrange(len(coins)):
                if amount-coins[value_index]>=0:
                    dp[amount]=min(dp[amount],1+dp[amount-coins[value_index]])
        
        if dp[len(dp)-1]==sys.maxint:
            return -1
        else:
            return dp[len(dp)-1]
