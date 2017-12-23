from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """ 
        i=0
        j=len(s)-1
        missing=len(t)
        tcount=Counter(t)
        start=0
        flg=False
        for end in xrange(len(s)):
            if s[end] in tcount:
                if tcount[s[end]]>0:
                    missing-=1
                tcount[s[end]]-=1
                
                

            #move the head pointers
            while missing==0:
                flg=True
                #print 'In for',start,end,s[start:end+1]
                if j-i>end-start:
                    i=start
                    j=end
                #case1:irrelavant char,can just move the head forward
                if s[start] not in tcount:
                    start+=1
                else:
                    #case1: can't move, if move head you will have missing
                    if tcount[s[start]]==0:
                        break
                    else:
                        tcount[s[start]]+=1
                        start+=1
        if flg:
            return s[i:j+1]
        else:
            return ""
                    
