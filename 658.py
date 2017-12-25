class Solution(object):
    #find the inserting index
    def bs(self,array,target):
        start=0
        end=len(array)-1
        while start<=end:
            mid=start+(end-start)/2
            if array[mid]==target:
                return mid
            elif array[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return start
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        target_index=self.bs(arr,x)
        print 'DEBUG1',target_index
        res=[]
        #2 corner cases,the insert index is out of the array
        #just return the first/last k elements
        if target_index==0:
            return arr[:k]
        if target_index==len(arr):
            return arr[-k:]
        
        right=target_index
        left=target_index-1
        
        print 'DEBUG',target_index,right,left

        while k>0:
            l=r=sys.maxint
            if left>=0:
                l=abs(x-arr[left])
            if right<len(arr):
                r=abs(x-arr[right])
            
            if l<=r:
                res.append(arr[left])
                left-=1
            else:
                res.append(arr[right])
                right+=1
            k-=1
        return sorted(res)
