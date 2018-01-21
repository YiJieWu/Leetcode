class Solution(object):
    def helper(self,array,start,end):
        while start<end:
            if array[start]!=array[end]:
                return False
            start+=1
            end-=1
        return True
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start=0
        end=len(s)-1
        while start<end:
            if s[start]!=s[end]:
                #try skip left & skip right
                if self.helper(s,start+1,end) or self.helper(s,start,end-1):
                    return True
                else:
                    return False   
            else:
                start+=1
                end-=1
        return True
