class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        mapping={}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j not in mapping:
                    mapping[i-j]=matrix[i][j]
                else:
                    if matrix[i][j] != mapping[i-j]:
                        return False
        return True
