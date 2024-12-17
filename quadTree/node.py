import numpy as np

class Node:
    """
    class representing a node in the quadtree.
    """
    def __init__(self, data, x0, x1, y0, y1, level):
        self.data = data
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.level = level
        self.children = []

    def is_leaf(self):
        """
        Checks if this node is a leaf node
        """
        if len(self.children) == 0:
            return True
        else:
            return False
    