class Solution(object):
    def helper(self,grid,x,y,res):
        #mark this as visited
        grid[x][y]=0
        res[0]+=1
        #try left,up,right,down
        if y-1>=0 and grid[x][y-1]==1:
            self.helper(grid,x,y-1,res)
        
        if x-1>=0 and grid[x-1][y]==1:
            self.helper(grid,x-1,y,res)
        
        if y+1<len(grid[0]) and grid[x][y+1]==1:
            self.helper(grid,x,y+1,res)
            
        if x+1<len(grid) and grid[x+1][y]==1:
            self.helper(grid,x+1,y,res)
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        res=0
        if len(grid)==0:
            return 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]==1:
                    r=[0]
                    self.helper(grid,i,j,r)
                    res=max(res,r[0])
        return res
