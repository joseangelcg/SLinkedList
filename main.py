from SLinkedList import SLinkedList

# Test code
if __name__ == '__main__':
    List1 = SLinkedList()
    List2 = SLinkedList()

    List1.append(5)
    List1.append(7)
    List1.append(8)
    List1.add_atindex(val=10, index=1)
    print(List1)

    List2.append_list(val_list=[20, 55, 84, 37])
    print(List2)

    print(List1 + List2)
    print("--------------------")
    print(List1)
    print(List2)
    print(List2 + List1)
    print("--------------------")
    List1 += 3
    print(List1)
    List1 -= 3
    print(List1)
