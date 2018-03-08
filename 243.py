class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1_index=w2_index=-1
        cur_min=1000000
        for index,word in enumerate(words):
            if word==word1:
                w1_index=index
            if word==word2:
                w2_index=index
            if w1_index!=-1 and w2_index !=-1:
                cur_min=min(cur_min,abs(w1_index-w2_index))
        return cur_min
                
