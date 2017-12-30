class Solution(object):
    def helper(self,amount,coins,start,res):
        #invalid case
        if amount<0:
            return
        if amount==0:
            res[0]+=1
            return
        for i in xrange(start,len(coins)):
            self.helper(amount-coins[i],coins,i,res)
            
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        res=[0]
        self.helper(amount,coins,0,res)
        return res[0]
