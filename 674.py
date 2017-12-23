class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        if len(nums)<=1:
            return len(nums)
        res=-1*sys.maxint
        start=0
        for end in xrange(1,len(nums)):
            if nums[end]<=nums[end-1]:
                if end-start>res:
                    res=end-start
                start=end

    return max(end-start+1,res)


