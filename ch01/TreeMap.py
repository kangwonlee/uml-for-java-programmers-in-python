class TreeNode(object):
    LESS = 0
    GREATER = 1
    def __init__(self, key, value):
        self.itsKey = key
        self.itsValue = value
        self.nodes = [None, None]

    def selectSubNode(self, key):
        if key < self.itsKey:
            result = self.LESS
        elif key > self.itsKey:
            result = self.GREATER
        else:
            assert key != self.itsKey, f"repr(key) = {repr(key)}, repr(self.itsKey) = {repr(self.itsKey)}"
        
        return result

    def find(self, key):
        if key == self.itsKey:
            result = self.itsValue
        else:
            result = self.findSubNodeForKey(self.selectSubNode(key), key)

        return result

    def findSubNodeForKey(self, node, key):
        if self.nodes[node] is None:
            result = None
        else:
            result = self.nodes[node].find(key)

        return result
