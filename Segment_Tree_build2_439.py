"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: A: a list of integer
    @return: The root of Segment Tree
    """
    def helper(self,array,start,end):
        if start>end:
            return None
        if start==end:
            return SegmentTreeNode(start,end,array[start])
        
        mid=start+(end-start)/2
        root=SegmentTreeNode(start,end,0)
        root.left=self.helper(array,start,mid)
        root.right=self.helper(array,mid+1,end)
        root.max=max(root.left.max,root.right.max)
        return root
        
    def build(self, A):
        # write your code here
        return self.helper(A,0,len(A)-1)
