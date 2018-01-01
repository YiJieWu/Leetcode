class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        
        """
        res=0
        hm={}
        hm[0]=1
        helper=[0]*(len(nums)+1)
        for i in xrange(1,len(helper)):
            #calculate the presum
            helper[i]+=helper[i-1]+nums[i-1]
            
            if helper[i]-k in hm:
                res+=hm[helper[i]-k]

            hm.setdefault(helper[i],0)
            hm[helper[i]]+=1

        return res
