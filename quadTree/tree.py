from quadTree.node import *
import numpy as np



"""
Source: 
    https://en.wikipedia.org/wiki/Quadtree
"""

class quadTree:
    """
    class representing a quadtree data structure
    """
    def __init__(self, size, maxDepth):
        self.size = size
        self.maxDepth = maxDepth
        self.root = None

    def Tree(self, data):
        """
        generates the quadtree structure based on the given 2D array of data.
        """
        self.root = self._recTree(data, 0, self.size - 1, 0, self.size - 1, 0)

    def _recTree(self, data, x0, x1, y0, y1, depth):
        """
        recursively generates nodes in the quadtree, splitting the region into 4 quadrants at each level.
        """
        if depth >= self.maxDepth or (x1 - x0 <= 1 and y1 - y0 <= 1):
            return Node(data[x0:x1 + 1, y0:y1 + 1], x0, x1, y0, y1, depth)

        midX = (x0 + x1) // 2
        midY = (y0 + y1) // 2

        node = Node(None, x0, x1, y0, y1, depth)

        #[q1    q2]
        #[q3    q4]
        node.children.append(self._recTree(data, x0, midX, y0, midY, depth + 1))#q1
        node.children.append(self._recTree(data, midX + 1, x1, y0, midY, depth + 1))#q2
        node.children.append(self._recTree(data, x0, midX, midY + 1, y1, depth + 1))#q3
        node.children.append(self._recTree(data, midX + 1, x1, midY + 1, y1, depth + 1))#q4

        return node

    def visualize(self, node, ax):
        """
        visualizes the quadtree by drawing each node's data on the given axes.
        nodes at higher levels are simplified for Level of Detail.
        """
        if node is None:
            return

        if node.is_leaf():
            if node.data is not None:
                ax.imshow(node.data, cmap='terrain', origin='lower', extent=[node.x0, node.x1, node.y0, node.y1])
        else:
            if node.level >= self.maxDepth - 2:
                if node.data is not None:
                    ax.imshow(node.data, cmap='terrain', origin='lower', extent=[node.x0, node.x1, node.y0, node.y1])
            else:
                avgHeight = np.mean(node.data) if node.data is not None else 0
                simpData = np.full((1, 1), avgHeight)
                ax.imshow(simpData, cmap='terrain', origin='lower', extent=[node.x0, node.x1, node.y0, node.y1])

        for child in node.children:
            self.visualize(child, ax)


