class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        myStack=[]
        res=[0]*len(temperatures)
        for i in xrange(len(temperatures)):
            #it means you find a greater temperature
            while(len(myStack)!=0 and temperatures[i]>temperatures[myStack[-1]]):
                index=myStack.pop()
                res[index]=i-index
            myStack.append(i)
        return res
                
