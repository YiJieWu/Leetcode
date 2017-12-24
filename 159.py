class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
      
        res=-1*sys.maxint
        dic={}
        start=end=0
        while end<len(s):
            #case1, you can keep pusing end 
            if s[end] not in dic and len(dic)<=1 or s[end] in dic:
                dic.setdefault(s[end], 0)
                dic[s[end]] += 1
                end+=1
            #you can not push end  but have to move start
            else:
                res=max(res,end-start)
                while len(dic)==2:
                    dic[s[start]]-=1
                    if dic[s[start]]==0:
                        del dic[s[start]]
                    start+=1
                    
        return max(res,end-start)
