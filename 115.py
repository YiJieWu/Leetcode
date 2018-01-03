'''
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''


#Naive recursion approach,TLE
class Solution(object):
    def helper(self,s,t,sindex,tindex):
        if tindex==len(t):
            return 1
        
        res=0
        for i in xrange(sindex,len(s)):
            if s[i]==t[tindex]:
                res+=self.helper(s,t,i+1,tindex+1)
        return res
                
            
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        return self.helper(s,t,0,0)
