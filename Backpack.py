class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        dp=[[False]*(m+1) for i in xrange(len(A)+1)]
        #initialize the first column to be 0
        for i in xrange(len(dp)):
            dp[i][0]=True
        
        for ele in xrange(1,len(dp)):
            for weight in xrange(1,len(dp[0])):
                #if i do not use the current item
                #then I check if by using the previous items if I can get to this weight
                dp[ele][weight]=dp[ele-1][weight]
                if weight-A[ele-1]>=0:
                    dp[ele][weight]=dp[ele][weight] or dp[ele-1][weight-A[ele-1]]
        #print dp
                    
        #Traverse the last row from end to begining
        for i in xrange(len(dp[0])-1,-1,-1):
            if dp[len(dp)-1][i]==True:
                return i
