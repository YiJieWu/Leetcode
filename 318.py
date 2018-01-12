class Solution(object):
    def check_not_in(self,words,index,set):
        for char in words[index]:
            if char in set:
                return False
        return True
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res=0
        if len(words)==0:
            return res
        
        for i in xrange(len(words)-1):
            myset=set(words[i])
            for j in xrange(i+1,len(words)):
                if self.check_not_in(words,j,myset):
                    res=max(res,len(words[i])*len(words[j]))
        return res
