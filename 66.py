class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        carry = 1
        for digit in reversed(digits):
            if digit+carry<10:
                res.insert(0,digit+carry)
                carry=0
            else:
                res.insert(0,digit+carry-10)
                carry=1
        if carry !=0:
            res.insert(0,carry)
        return res
