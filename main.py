from SLinkedList import SLinkedList

# Test code
if __name__ == '__main__':
    List1 = SLinkedList()
    List1.addVal(5)
    List1.addVal(7)
    List1.addVal(8)
    print(List1)
    print(len(List1))

    List1.removeVal(5)
    print(List1)
    print(len(List1))
    print(List1.get(2))
