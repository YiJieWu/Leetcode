class Solution:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res=[0]*length
        for update in updates:
            start_index=update[0]
            end_index=update[1]
            incre=update[2]
            res[start_index]+=incre
            if end_index+1<len(res):
                res[end_index+1]-=incre
        print(res)
        for index in range(1,len(res)):
            res[index]+=res[index-1]
        
        return res
