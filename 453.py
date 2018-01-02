from collections import deque
class Solution(object):
    def check_stop(self,array):
        for i in xrange(1,len(array)):
            if array[i]!=array[0]:
                return False
        return True
    
    #update the given array except the index 
    def update(self,array,index):
        l=[0]*len(array)
        for i in xrange(len(l)):
            if i!=index:
                l[i]=array[i]+1
            else:
                l[i]=array[i]
        return l
    
    def helper(self,nums,queue,step):
        queue.append(nums)
        while len(queue)!=0:
            #print 'In queue',queue,step
            level_count=len(queue)
            while level_count!=0:
                cur=queue.popleft()
                level_count-=1
                #check if the ending condition can be satisfied,which is all ele EQUAL
                if self.check_stop(cur):
                    return step
                #select the index will not be incremented,and insert it into the Queue
                for i in xrange(len(cur)):
                    queue.append(self.update(cur,i))
            step+=1
                    
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Queue=deque()
        return self.helper(nums,Queue,0)
