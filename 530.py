# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,root,prev,res):
        if root==None:
            return
        self.helper(root.left,prev,res)
        if prev[0]!=-1:
            res[0]=min(res[0],root.val-prev[0])
        prev[0]=root.val
        self.helper(root.right,prev,res)
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[sys.maxint]
        self.helper(root,[-1],res)
        return res[0]
