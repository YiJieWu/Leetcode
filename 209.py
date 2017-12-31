class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res=sys.maxint
        cur=0
        start=0
        for end in xrange(len(nums)):
            cur+=nums[end]
            while cur>=s:
                res=min(res,end-start+1)
                cur-=nums[start]
                start+=1
        if res==sys.maxint:
            return 0
        return res
