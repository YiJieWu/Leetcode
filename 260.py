# naive approach, using python counter

from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        cnt = Counter(nums)
        for key in cnt:
            if cnt[key] == 1:
                res.append(key)
        return res
