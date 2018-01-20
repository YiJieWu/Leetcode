# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#The naive approach traversing the whole tree got TLE
class Solution(object):
    def helper(self,root,res):
        if root==None:
            return
        res[0]+=1
        self.helper(root.left,res)
        self.helper(root.right,res)
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[0]
        self.helper(root,res)
        return res[0]
        
