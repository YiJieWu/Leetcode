import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap=[]
        self.minheap=[]
    
    '''
    Thinking about the balancing part case by case
    There will be only 2 cases for the initial conditions
    '''

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """

        #Step1:push the ele into the maxheap
        heapq.heappush(self.maxheap,-1.0*num)
        
        #Step2:matain balancing
        heapq.heappush(self.minheap,-1.0*heapq.heappop(self.maxheap))
        
        #Step3:check if you need to reba;ance
        if len(self.maxheap)<len(self.minheap):
            heapq.heappush(self.maxheap,-1.0*heapq.heappop(self.minheap))
            
 

        

    def findMedian(self):
        """
        :rtype: float
        """
        maxhead=minhead=0.0
        if len(self.maxheap)!=0:
            maxhead=heapq.heappop(self.maxheap)
            heapq.heappush(self.maxheap,maxhead)
        if len(self.minheap)!=0:
            minhead=heapq.heappop(self.minheap)
            heapq.heappush(self.minheap,minhead)
        #even number of eles
        if (len(self.maxheap)+len(self.minheap))%2==0:
            return (-1.0*maxhead+minhead)/2
        else:
            return -1.0*maxhead
