class Solution(object):
    def helper(self, S, start, end, cur,res):
        if start==end:
            res.append(cur)
            return
        if S[start].isalpha():
            self.helper(S,start+1,end,cur+S[start].lower(), res)
            self.helper(S,start+1,end,cur+S[start].upper(), res)
        else:
            self.helper(S,start+1,end,cur+S[start], res)
            
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res=[]
        self.helper(S,0,len(S),"",res)
        return res
