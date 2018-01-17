#Brutal force recursion

class Solution(object):
    def helper(self,s,wordDict,start,cur,res):
        if start==len(s):
            res.append((cur))
            return
        
        for end in xrange(start+1,len(s)+1):
            if s[start:end] in wordDict:
                if end!=len(s):
                    self.helper(s,wordDict,end,cur+s[start:end]+" ",res)
                else:
                    self.helper(s,wordDict,end,cur+s[start:end],res)

               
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res=[]
        self.helper(s,wordDict,0,"",res)
        return res



#meomrization dp

class Solution(object):
    def helper(self,s,wordDict,start,cur,res,dp):
        if start==len(s):
            res.append((cur))
            return True
        r=False
        for end in xrange(start+1,len(s)+1):
            if s[start:end] in wordDict:
                if dp[end]!=False:
                    if end!=len(s):
                        dp[end]=self.helper(s,wordDict,end,cur+s[start:end]+" ",res,dp)
                    else:
                        dp[end]=self.helper(s,wordDict,end,cur+s[start:end],res,dp)
                r=r or dp[end]

        return r
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res=[]
        dp=[None]*(len(s)+1)
        self.helper(s,wordDict,0,"",res,dp)
        return res
