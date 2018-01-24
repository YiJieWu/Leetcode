class Solution(object):
    #there are k section I need to get, each seaction need to get exact target
    def helper(self,array,ksection,target,myset,k,start):
        #print 'in helper',ksection,target
        if ksection==1 and target==0:
            return True
        if target<0:
            return False
        if target==0:
            return self.helper(array,ksection-1,sum(array)/k,myset,k,0)
            
        
        for index in xrange(start,len(array)):
            if  index not in myset:
                myset.add(index)
                if self.helper(array,ksection,target-array[index],myset,k,index+1):
                    return True
                myset.remove(index)
        return False
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        total=sum(nums)
        if total%k!=0:
            return False
        return self.helper(nums,k,total/k,set(),k,0)
