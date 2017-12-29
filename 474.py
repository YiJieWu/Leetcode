from collections import Counter
class Solution(object):
    def helper(self,input,m,n,index,target):
        if index==target:
            return 0
        used=not_used=0
        if m-input[index][0]>=0 and n-input[index][1]>=0:
            used=1+self.helper(input,m-input[index][0],n-input[index][1],index+1,target)
        not_used=self.helper(input,m,n,index+1,target)
        return max(used,not_used)
        
        
            
    def extract(self,word):
        c=Counter(word)
        return (c['0'],c['1'])
    
    def preprocess(self,strs):
        res=[]
        c1=c2=0
        for word in strs:
            t=self.extract(word)
            res.append(t)
            c1+=t[0]
            c2+=t[1]
        return res,c1,c2
    
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        input,c1,c2=self.preprocess(strs)
        return self.helper(input,m,n,0,len(input))
        
