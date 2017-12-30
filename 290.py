class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        hm={}
        str=str.split(' ')
        if len(pattern)!=len(str):
            return False
        for i in xrange(len(pattern)):
            if pattern[i] not in hm:
                if str[i] in hm.values():

                    return False
                hm[pattern[i]]=str[i]
            else:
                if str[i]!=hm[pattern[i]]:
                    return False
            
        return True
