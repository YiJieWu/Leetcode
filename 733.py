class Solution(object):
    def helper(self,input,x,y,old,new):
        input[x][y]=new
        #check left,up,right,down
        if y-1>=0 and input[x][y-1]==old:
            self.helper(input,x,y-1,old,new)
        if x-1>=0 and input[x-1][y]==old:
            self.helper(input,x-1,y,old,new)
        if y+1<len(input[0]) and input[x][y+1]==old:
            self.helper(input,x,y+1,old,new)
        if x+1<len(input) and input[x+1][y]==old:
            self.helper(input,x+1,y,old,new)

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc]==newColor:
            return image
        self.helper(image,sr,sc,image[sr][sc],newColor)
        return image
