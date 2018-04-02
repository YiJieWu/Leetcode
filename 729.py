class MyCalendar:
    def __init__(self):
        self.l=[]
        
    # return -1 indicate not able to insert, otherwise return the insertion index
    def insert_position(self,target):
        start=0
        end=len(self.l)-1
        while start<=end:
            mid=start+(end-start)/2
            if target==self.l[mid][1]:
                return mid+1
            elif target>self.l[mid][1]:
                start=mid+1
            else:
                if target<self.l[mid][0]:
                    end=mid-1
                else:
                    return -1
        return start
            

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.l)==0:
            self.l.append((start,end))
            return True
        else:
            pos=self.insert_position(start)
            if pos != -1:
                # check if there is enough room for inserting
                if  pos == len(self.l) or pos != len(self.l) and end<=self.l[pos][0]:
                    self.l.insert(pos,(start,end))
                    return True
            return False







# second approach, this is really a cool approah to handle edge cases


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    

class MyCalendar(object):
    def __init__(self):
        self.root = None
    
    def insert(self,root ,node):
        if node.start >= root.end:
            if  root.right==None:
                root.right = node
                return True
            return self.insert(root.right,node)
        elif node.end <= root.start:
            if  root.left==None:
                root.left = node
                return True
            return self.insert(root.left,node)
        else:
            return False

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.insert(self.root,Node(start, end))
