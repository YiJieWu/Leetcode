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
#########################################################
from collections import Counter
class Solution(object):
    def helper(self,input,m,n,index,target,dp):
        if index==target:
            return 0
        if dp[index][m][n]!=0:
            return dp[index][m][n]
        used=not_used=0
        if m-input[index][0]>=0 and n-input[index][1]>=0:
            used=1+self.helper(input,m-input[index][0],n-input[index][1],index+1,target,dp)
        not_used=self.helper(input,m,n,index+1,target,dp)
        dp[index][m][n]=max(used,not_used)
        return dp[index][m][n]
        
            
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
        dp=[[[0]*(n+1) for i in xrange(m+1)] for z in xrange(len(strs)+1) ]
        return self.helper(input,m,n,0,len(input),dp)
        
             

#########################################################
class Solution(object):
    def helper(self,word):
        zc=oc=0
        for char in word:
            if char=='0':
                zc+=1
            else:
                oc+=1
        return zc,oc
    
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[[0]*(n+1) for i in xrange(m+1)] for i in xrange(len(strs)+1)]
        for i in xrange(1,len(dp)):
            for j in xrange(len(dp[0])):
                for k in xrange(len(dp[0][0])):
                    dp[i][j][k]=dp[i-1][j][k]
                    zero_count,one_count=self.helper(strs[i-1])
                    if j-zero_count>=0 and k-one_count>=0:
                        dp[i][j][k]=max(dp[i][j][k],1+dp[i-1][j-zero_count][k-one_count])
                        
        return dp[len(dp)-1][m][n]
