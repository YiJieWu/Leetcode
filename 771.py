class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        jewel_set=set(J)
        for char in S:
            if char in jewel_set:
                count+=1
        return count
