class TreeNode(object):
    LESS = 0
    GREATER = 1

    def __init__(self, key, value):
        self.itsKey = key
        self.itsValue = value
        self.nodes = [None, None]

    def __del__(self):
        # TODO : what if circular reference happens?
        del self.itsKey
        del self.itsValue
        del self.nodes[:]
        del self.nodes

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

    def add(self, key, value):
        if key == self.itsKey:
            self.itsValue = value
        else:
            self.addSubNode(self.selectSubNode(key), key, value)

    def addSubNode(self, node, key, value):
        if self.nodes[node] is None:
            self.nodes[node] = TreeNode(key, value)
        else:
            self.nodes[node].add(key, value)
