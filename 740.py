
# naive approach, got reach max recursion depth
class Solution(object):
    def mark(self,flag,nums,index):
        s=set()
        for i,num in enumerate(nums):
            if flag[i]==1 and (num==nums[index]+1 or num==nums[index]-1 or i==index):
                flag[i]=0
                s.add(i)
        return s
                
    def unmark(self,flag,nums,index):
        for i in range(len(nums)):
            if i in index:
                flag[i]=1
    
    def helper(self,nums,flag):
        earn=0
        for index,num in enumerate(nums):
            #can visit
            if flag[index]==1:
                s=self.mark(flag,nums,index)
                earn=max(earn,num+self.helper(nums,flag))
                self.unmark(flag,nums,s)
        return earn
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag=[1]*len(nums)
        return self.helper(nums,flag)
