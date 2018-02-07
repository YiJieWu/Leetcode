class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest=index=-1
        for i,num in enumerate(nums):
            if num>largest:
                largest=num
                index=i
        for i,num in enumerate(nums):
            if largest<2*num and i!=index:
                return -1
        return index
