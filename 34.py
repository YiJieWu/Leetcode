class Solution(object):
    def helper(self,nums,target,start,end,direction):
        index=-1
        while start<=end:
            mid=start+(end-start)/2
            if nums[mid]==target:
                index=mid
                #still push left
                if direction==0:
                    end=mid-1
                else:
                    start=mid+1
                    
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
                    
                    
        return index
      
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[-1,-1]
        if len(nums)==0:
            return res
        left=self.helper(nums,target,0,len(nums)-1,0)
        right=self.helper(nums,target,0,len(nums)-1,1)
        return [left,right]
