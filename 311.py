#Naive approach, do the multiplication without any optimization,TLE
#Becasue when the matrix is really sparce, which means when there's lots
#of 0 within the matrix, you are waste your time on those 0s


class Solution(object):
    def calculate(self,A,B,rowA,colB):
        res=0
        for i in xrange(len(A[0])):
            res+=A[rowA][i]*B[i][colB]
        return res
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        #create the result matrix
        res=[[0]*len(B[0]) for i in xrange(len(A))]
        #Do the multiplication
        for rowA in xrange(len(A)):
            for colB in xrange(len(B[0])):
                res[rowA][colB]=self.calculate(A,B,rowA,colB)
        return res
