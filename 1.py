class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm={}
        res=[]

        for i in xrange(len(nums)):
            if target-nums[i] in hm :
                res.append(i)
                res.append(hm[target-nums[i]])
            if nums[i] not in hm:
                hm[nums[i]]=i  
        return res
