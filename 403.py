#naive brutal force appraoch,got TLE
class Solution:
    def getIndex(self,stones,val,start,end):
        while start<=end:
            mid=start+(end-start)//2
            if stones[mid]==val:
                return mid
            elif val<stones[mid]:
                end=mid-1
            else:
                start=mid+1
        return -1
    
    def helper(self,stones,start,units):
        #in or exceed the last stone's position
        if start==len(stones)-1:
            return True
        
        for step in range(units-1,units+2):
            if stones[start]+step>stones[start]:
                newstart=self.getIndex(stones,stones[start]+step,start,len(stones)-1)
                if newstart!=-1 and self.helper(stones,newstart,step):
                    return True
        return False
            
        
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        return self.helper(stones,0,0)





#2d dp version
class Solution:
    def getIndex(self,stones,val,start,end):
        while start<=end:
            mid=start+(end-start)//2
            if stones[mid]==val:
                return mid
            elif val<stones[mid]:
                end=mid-1
            else:
                start=mid+1
        return -1
    
    def helper(self,stones,start,units,dp):
        #in or exceed the last stone's position
        if start==len(stones)-1:
            return True
        #print ('in helper',start,dp)
        if dp[units][start]==None:
            for step in range(units-1,units+2):
                if stones[start]+step>stones[start]:
                    newstart=self.getIndex(stones,stones[start]+step,start,len(stones)-1)
                    #print('newx',newstart,step)
                    if newstart!=-1 and self.helper(stones,newstart,step,dp):
                        return True
        dp[units][start]=False
        return dp[units][start]
            
        
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dp=[[None]*len(stones) for i in range(0,len(stones))]
        return self.helper(stones,0,0,dp)
