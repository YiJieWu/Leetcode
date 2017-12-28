class Solution:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        #I want use dp[i][j] to denote by using the top i element
        # what's the max value I can get given the constraint the bag is of size j
        
        dp=[[0]*(m+1) for i in xrange(len(A)+1)]
        for i in xrange(1,len(dp)):
            for j in xrange(1,len(dp[0])):
                #case one, if I do not use current ele i
                dp[i][j]=dp[i-1][j]
                #case two, if I use current ele i
                if j-A[i-1]>=0:
                    dp[i][j]=max(dp[i][j],dp[i-1][j-A[i-1]]+V[i-1])
        #print dp
        res=-1*sys.maxint
        for i in xrange(1,len(dp[0])):
            res=max(res,dp[len(dp)-1][i])
        return res
