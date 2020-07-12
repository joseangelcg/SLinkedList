from Node import Node


class SLinkedList:
    """docstring fos SLinkedList"""

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        self._node_iter = self._head
        return self

    def __next__(self):
        if self._node_iter is None:
            raise StopIteration
        to_ret = self._node_iter
        self._node_iter = self._node_iter.next
        return to_ret

    def containsval(self, val):
        """
                Searches for a specific value in the current List

                Return value:
                        True if val exists in SlinkedList instance
                        False otherwise
        """
        for node in self:
            if node.val == val:
                return True
        return False

    def removeval(self, val):
        """
                Removes val in the current List
                If val is not in the list, nothing happens

                Return value:
                        None
        """
        if self._head is None:
            raise RuntimeError("Object %s: Can't remove value from empty list" % self.__class__.__name__)
        else:
            if self.containsval(val):
                if self._size == 1:
                    del self._head
                    self._head = None
                else:
                    prev = None
                    for a in self:
                        if a.val != val:
                            prev = a
                        else:
                            if prev is None:
                                self._head = a.next
                            else:
                                prev.setnext(a.next)
                            del a
                            break
                self._size -= 1

    def join(self, other):
        if not isinstance(other, SLinkedList):
            raise TypeError("%s: Only SLinkedList can be joined together" % self.__class__.__name__)
        else:
            for node in self:
                if node.next is None:
                    node.setnext(other._head)
                    break

    def append_list(self, val_list):
        if not isinstance(val_list, list):
            raise TypeError("%s: Wrong data type" % self.__class__.__name__)
        else:
            for elem in val_list:
                self.append(elem)

    def append(self, val):
        temp = Node(val)
        if self._head is None:
            self._head = temp
        else:
            for node in self:
                if node.next is None:
                    node.setnext(temp)
                    break
        self._size += 1

    def add_atindex(self, val, index):
        if not isinstance(index, int):
            raise TypeError("%s: Wrong data type" % self.__class__.__name__)
        elif index >= len(self):
            raise IndexError("%s: Index out of bonds" % self.__class__.__name__)
        else:
            prev = None
            for node in self:
                if index > 0:
                    prev = node
                    index -= 1
                else:
                    if prev is None:
                        new = Node(val, self._head)
                        self._head = new
                    else:
                        new = Node(val, node)
                        prev.setnext(new)
                    break

    def getindex(self, index):
        if not isinstance(index, int):
            raise TypeError("%s: Wrong data type" % self.__class__.__name__)
        elif index >= len(self):
            raise IndexError("%s: Index out of bonds" % self.__class__.__name__)
        else:
            for node in self:
                if index == 0:
                    return node.val
                index -= 1

    def __repr__(self):
        return "< {}: list = {}, size = {} >".format(self.__class__.__name__, self.__str__(), len(self))

    def __str__(self):
        s = []
        for val in self:
            s.append(str(val))
        return "->".join(s)

    def __add__(self, other):
        ret_list = SLinkedList()
        for node in self:
            ret_list.append(node.val)
        ret_list.join(other)
        return ret_list

    def __iadd__(self, other):
        self.append(other)
        return self

    def __isub__(self, other):
        self.removeval(other)
        return self
