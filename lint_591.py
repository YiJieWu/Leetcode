# the weight approach, always connect the root of a smaller tree to a larget tree
class ConnectingGraph3:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.count=n
        self.array=[i for i in range(n+1)]
        self.size=[1]*(n+1)



    def root(self,a):
        while self.array[a] != a:
            a=self.array[a]
        return a


    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
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

    """
    @return: An integer
    """
    def query(self):
        # write your code here
        return self.count

