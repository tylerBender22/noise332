

class Node:
    def __init__(self, x, y, data=None):
        self.x = x
        self.y = y
        self.data = data
        self.children = [None, None, None, None]


    def isLeaf(self) -> bool:
        return all(child is None for child in self.children)
    

        
