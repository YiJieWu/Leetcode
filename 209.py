'''
注意这两道题在哪个地方计算res

'''




'''
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.
'''




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


'''
Given an array of n positive integers and a positive integer k, 
find the max length of a contiguous subarray of which the sum <= k. 
'''
def my(self,arr,k):
    res=-1*sys.maxint
    cursum=0
    start=0
    for end in range(len(arr)):
        cursum+=arr[end]
        while cursum>k:
            cursum-=arr[start]
            start+=1
        
        res=max(res,end-start+1)

    return res