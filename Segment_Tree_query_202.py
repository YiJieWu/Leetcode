"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of segment tree.
    @param: start: start value.
    @param: end: end value.
    @return: The maximum number in the interval [start, end]
    """
    def query(self, root, start, end):
        # write your code here
        if root.start==start and root.end==end:
            return root.max
        
        mid=root.start+(root.end-root.start)/2
        #search in the left
        if end<=mid:
            return self.query(root.left,start,end)
        elif start>mid:
            return self.query(root.right,start,end)
        else:
            return max(self.query(root.left,start,mid),self.query(root.right,mid+1,end))
