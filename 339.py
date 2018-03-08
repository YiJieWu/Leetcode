class Solution(object):
    def DFS(self,nestedList,depth):
        cursum=0
        for ele in nestedList:
            #if it's a single int
            if ele.isInteger():
                cursum+=depth*ele.getInteger()
            else:
                cursum+=self.DFS(ele.getList(),depth+1)
        return cursum
    
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.DFS(nestedList,1)
