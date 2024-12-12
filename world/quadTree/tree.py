from quadTree.node import *
class quadTree:
    def __init__(self, head):
        self.head = head

    def doTree(self, x, y, size):
        self.head = self._doTreeRec(x, y, size)
        return self
    
    def _doTreeRec(self, x, y, size):
        halfSize = size // 2
        q00 = self._doTreeRec(x, y, halfSize)
        q01 = self._doTreeRec(x + halfSize, y, halfSize)
        q10 = self._doTreeRec(x, y + halfSize, halfSize)
        q11 = self._doTreeRec(x + halfSize, y + halfSize, halfSize)

        node = Node(x, y, size)
        node.children = [q00, q01, q10, q11]
        return node