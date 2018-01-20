class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end=len(nums)-1
        while start<end:
            mid=start+(end-start)/2
            #case 1, hit solution, this is the single num
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            #case2 
            elif nums[mid]==nums[mid-1]:
                if mid%2==1:
                    start=mid+1
                else:
                    end=mid-1
            else:
                if mid%2==0:
                    start=mid+1
                else:
                    end=mid-1
        return nums[start]
