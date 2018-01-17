class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        dp=[1]*len(nums)
        for i in xrange(1,len(dp)):
            for j in xrange(i):
                #increasing
                if nums[i]>nums[j] and 1+dp[j]>dp[i]:
                    dp[i]=1+dp[j]
           
       
        return max(dp)
        
