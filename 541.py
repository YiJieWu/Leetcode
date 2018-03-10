class Solution(object):
    def reverse(self,s,start,end):
        while start<end:
            e=s[end]
            s[end]=s[start]
            s[start]=e
            start+=1
            end-=1

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        t_length=len(s)
        start=0
        s=list(s)
        while t_length-2*k>=0:
            #reverse the first k
            self.reverse(s,start,start+k-1)
            start+=2*k
            t_length-=2*k
            
        if t_length !=0:
            print t_length
            if t_length<k:
                self.reverse(s,start,len(s)-1)
            else:
                self.reverse(s,start,start+k-1)
        return "".join(s)
