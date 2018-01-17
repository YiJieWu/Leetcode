#first recursion try got TLE
class Solution(object):
    def helper(self,s,wordDict,start):
        if start==len(s):
            return True
        res=False
        for end in xrange(start+1,len(s)+1):
            if s[start:end] in wordDict:
                res=res or self.helper(s,wordDict,end)
        return res
                
                
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.helper(s,wordDict,0)




#Actually, a better version of the brutal force recursion will be this
#Once you hit True, you return directly

class Solution(object):
    def helper(self,s,wordDict,start):
        if start==len(s):
            return True
        for end in xrange(start+1,len(s)+1):
            if s[start:end] in wordDict:
                if self.helper(s,wordDict,end):
                    return True
        return False
                
                
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.helper(s,wordDict,0)


'''
Original thought!!!

Thinking about using the memorization technique when dp[i]
will denote whether you can make it starting from the ith 
index, BUT the big concern I have right now is this will not
help because this question is asking me to check whether a 
route exists rather than like what is the shortest,which means
there will be not duplicate sub-problems since once I found a
route I will return
'''



'''
But actually this memorization version works!WHY????
You are actually half right, but you are only considering the
case when they return TRUE, but what if when sometimes you can not 
reach to the end
e.g

case1:
s=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
dic={a,aa,aaa}

VS

case2:
s=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab
dic={a,aa,aaa}

In case1 scenario, you original thoght is correct, even you use
the dp memorization trick, you are not gaining any advantage from it
when compared with the original naive brutal force solution.

HOWEVER, let's pay attention to the case2 scenario, when you keep trying 
something and in the end, you realize that this route does not work, in the brutal 
force solution,when the function returns from the calling stack to some previous
start index, you will recalculating those dead end path down to the leaf, lots of
redundant and overlapping calculation.
On the other hand, when you apply the memorization trick on the dp solution, you avoid
recalculating those dead path because whenever you you reach to dp[i], it will tell you 
whether you can reach the end/leaf node of this tree!!!!!!!!


'''


class Solution(object):
    def helper(self,s,wordDict,start,dp):
        if start==len(s):
            return True
        res=False
        for end in xrange(start+1,len(s)+1):
            if s[start:end] in wordDict:
                if dp[end]==None:
                    dp[end]=self.helper(s,wordDict,end,dp)
                res=res or dp[end]
        return res
                
                
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp=[None]*(len(s)+1)
        return self.helper(s,wordDict,0,dp)


'''
The bottom up dp version of this problem is actually hard, the key of the elegant bottom up
version of this probelm is correctly defined what dp[i] means. Originally, I was thinking dp[i]
will denote the suarray ending at index i, just like the longest increasing subsequence problem,
then I realize it's actually hard, the better way is to define dp[i] as the len of subarray of
length i, I actually want to REDO this question later!!
'''
