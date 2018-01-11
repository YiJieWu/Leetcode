class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        hm={}
        for index,num in enumerate(B):
            hm.setdefault(num,[])
            hm[num].append(index)
        res=[]
        for num in A:
            if num in hm:
                res.append(hm[num].pop())
                if len(hm[num])==0:
                    del hm[num]
        return res
