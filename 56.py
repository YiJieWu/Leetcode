# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res=[]
        new=sorted(intervals,key=lambda interval:interval.start)
        if len(new)<=1:
            return intervals
        start=new[0].start
        end=new[0].end
        for i in xrange(1,len(new)):
            if new[i].start>end:
                res.append(Interval(start,end))
                start=new[i].start
                end=new[i].end
            else:
                end=max(end,new[i].end)
            
        res.append(Interval(start,end))
        return res
