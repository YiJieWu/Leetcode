class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        l=len(pairs)
        if l<=1:
            return l
        #sort the list of pairs by the first ele
        pairs.sort(key=lambda ele:ele[0])
        #create the dp helper array:
        dp=[1]*l
        for i in xrange(1,l):
            for j in xrange(i):
                if pairs[i][0]>pairs[j][1]:
                    dp[i]=max(dp[i],1+dp[j])
        return max(dp)
