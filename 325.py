class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hm={}
        #filled the dummy head value
        hm[0]=0
        res=-1*sys.maxint
        helper=[0]*(len(nums)+1)
        for i in xrange(1,len(helper)):
            #calculate the presum
            helper[i]+=helper[i-1]+nums[i-1]
            
            if helper[i]-k in hm:
                res=max(res,i-hm[helper[i]-k])
            
            if helper[i] not in hm:
                hm[helper[i]]=i
        
        if res==-1*sys.maxint:
            return 0
        else:
            return res
