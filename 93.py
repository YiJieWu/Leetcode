class Solution(object):
    #given a string, return if it's a valid ip
    def valid(self,string):
        #any ip starts with 0 but not 0 is invalid
        if string[0]=='0' and len(string)>1:
            return False
        if int(string)>255:
            return False
        return True
        
    def helper(self,s,section,start,end,cur,res):        
        if start==end:
            if section==4:
                res.append(cur[0:len(cur)-1])
            return 
        
        if section==4:
            return 

        
        for nextstart in xrange(start+1,min(start+4,end+1)):
            string=s[start:nextstart]
            #print 'slicing',start,nextstart,string
            #check if this slice is indeed a valid ip address
            if self.valid(string):
                self.helper(s,section+1,nextstart,end,cur+string+'.',res)
                
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        res=[]
        self.helper(s,0,0,len(s),"",res)
        return res
