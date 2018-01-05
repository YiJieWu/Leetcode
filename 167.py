#主要是利用了array is sorted 的这个property
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(numbers)==0:
            return []
        start=0
        end=len(numbers)-1
        while start<=end:
            cursum=numbers[start]+numbers[end]
            if cursum==target:
                return [start+1,end+1]
            elif cursum<target:
                start+=1
            else:
                end-=1
        return []
