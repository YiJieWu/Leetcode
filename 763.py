class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        range_dic={}
        for i in range(len(S)):
            range_dic.setdefault(S[i],i)
            range_dic[S[i]]=i
        res=[]
        furthest=0
        count=0
        for i in range(len(S)):
            furthest= max(furthest,range_dic[S[i]])
            count+=1
            
            if i==furthest:
                res.append(count)
                furthest=0
                count=0
        return res
                
