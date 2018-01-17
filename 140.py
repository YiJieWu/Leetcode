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
