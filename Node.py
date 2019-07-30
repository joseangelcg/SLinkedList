class Node:
    """docstring for Node"""

    def __init__(self, val):
        self.val = val
        self.next = None

    def setNext(self, node):
        self.next = node

    def setValue(self, val):
        if self is not None:
            self.val = val

    def __repr__(self):
        return str(self.val)
