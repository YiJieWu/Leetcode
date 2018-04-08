# union find approach with weighted quick union

class Union_find(object):
    def __init__(self,n):
        self.count=n
        self.array=[i for i in range(n+1)]
        self.size=[1]*(n+1)
        
    def root(self,a):
        while self.array[a] != a:
            self.array[a]=self.array[self.array[a]]
            a=self.array[a]
        return a

    def union(self, a, b):
        r1=self.root(a)
        r2=self.root(b)
        if r1 != r2:
            self.count-=1
            if self.size[r1] <= self.size[r2]:
                self.size[r2]+=self.size[r1]
                self.array[r1]=r2
            else:
                self.size[r1]+=self.size[r2]
                self.array[r2]=r1

                
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf=Union_find(n)
        for edge in edges:
            uf.union(edge[0],edge[1])
        return uf.count
