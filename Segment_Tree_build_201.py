"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        # write your code here
        if start>end:
            return None
        if start==end:
            return SegmentTreeNode(start,end)
        
        mid=start+(end-start)/2
        root=SegmentTreeNode(start,end)
        root.left=self.build(start,mid)
        root.right=self.build(mid+1,end)
        return root
