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






#second try
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s)==0:
            return ""
        
        remaining=len(t)
        c=Counter(t)
        start=end=0
        min_index=[0,len(s)-1]
        for end,char in enumerate(s):
            if char in c:
                if c[char]>0:
                    remaining-=1
                c[char]-=1
                
            if remaining==0:
                while start<end:
                    if s[start] not in c:
                        start+=1
                    else:
                        if c[s[start]]<0:
                            c[s[start]]+=1
                            start+=1
                        else:
                            break
                if end-start<min_index[1]-min_index[0]:
                    min_index[0]=start
                    min_index[1]=end
        if remaining!=0:
            return ""
        else:
            return s[min_index[0]:min_index[1]+1]                    
