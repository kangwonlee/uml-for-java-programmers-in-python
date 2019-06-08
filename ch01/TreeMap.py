class TreeNode(object):
    LESS = 0
    GREATER = 1
    def __init__(self, key, value):
        self.itsKey = key
        self.itsValue = value
        self.nodes = [None, None]
