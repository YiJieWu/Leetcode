class Solution(object):
    def helper(self,nums,prev,cur,index):
        if len(cur)==3:
            return True
        if index==len(nums) and len(cur)!=3:
            return False
        
        take=not_take=False
        if nums[index]>prev:
            cur.append(nums[index])
            take=self.helper(nums,nums[index],cur,index+1)
            cur.pop()
        not_take=self.helper(nums,prev,cur,index+1)
        return take or not_take
            
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.helper(nums,-1*sys.maxint,[],0)



########################################################
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s1=s2=sys.maxint
        for num in nums:
            if num<=s1:
                s1=num
            elif num<=s2:
                s2=num
            else:
                return True
        return False
