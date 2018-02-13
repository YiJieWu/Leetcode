class Solution(object):
    #return True if start and end differs only in 1 character
    def verify(self,start,end):
        count=0
        for index in range(len(start)):
            if start[index]!=end[index]:
                count+=1
            if count>1:
                return False
        return True
        
    
    def helper(self,start,end,bank,flag):
        if start==end:
            return 0
     
        res=1000000
        for index,cur_str in enumerate(bank):
            #Make sure this move is a valid move
            if flag[index]==0 and self.verify(start,cur_str):
                #set the current string in the bank to be visited
                flag[index]=1
                bench=self.helper(cur_str,end,bank,flag)
                if bench !=-1:
                    res=min(res,1+bench)
                flag[index]=0
        if res!=1000000:        
            return res
        else:
            return -1
        
            
        
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        flag=[0]*len(bank)
        return self.helper(start,end,bank,flag)
