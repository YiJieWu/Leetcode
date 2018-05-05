class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        mi_list=[]
        ma_list=[]
        for row in range(len(arrays)):
            mi_list.append((arrays[row][0],row))
            ma_list.append((arrays[row][len(arrays[row])-1],row))
        
        if ma_list[0]> ma_list[1]:
            maxx=0
            second_max=1
        else:
            maxx=1
            second_max=0
        
        if mi_list[0]<mi_list[1]:
            minn=0
            second_min=1
        else:
            minn=1
            second_min=0
        for index in range(len(ma_list)):
            if ma_list[index]>ma_list[maxx]:
                second_max=maxx
                maxx=index
            elif ma_list[index]>ma_list[second_max] and ma_list[index]<ma_list[maxx]:
                second_max=index
                
            if mi_list[index]<mi_list[minn]:
                second_min=minn
                minn=index
            elif mi_list[index]<mi_list[second_min] and mi_list[index]>mi_list[minn]:
                second_min=index
        
 
        return abs(ma_list[maxx][0]-mi_list[minn][0]) if ma_list[maxx][1] != mi_list[minn][1] else max(abs(ma_list[maxx][0]-mi_list[second_min][0]),abs(mi_list[minn][0]-ma_list[second_max][0]))
