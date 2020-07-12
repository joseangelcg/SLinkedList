class Node:
    """docstring for Node"""

    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def setnext(self, node):
        self.next = node

    def setvalue(self, val):
        if self is not None:
            self.val = val

    def __str__(self):
        return "[ {} ]".format(str(self.val))
