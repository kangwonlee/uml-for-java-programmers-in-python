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
