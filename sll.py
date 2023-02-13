# Name: Hannah Rummel
# OSU Email: rummelh@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 2/13/2023
# Description: Linked list class


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """inserts value after sentinel node"""
        current_node = SLNode(value)
        current_node.next = self._head.next
        self._head.next = current_node

    def insert_back(self, value: object) -> None:
        """inserts value at end of linkedlist"""
        current_node = self._head
        while current_node is not None:
            #transverses list while checking to make sure current node is not end.
            if current_node.next is None:
                #if next node is None, we are at end
                add_val = SLNode(value)
                current_node.next = add_val
                add_val.next = None
                return
            current_node = current_node.next

    def insert_at_index(self, index: int, value: object) -> None:
        """insert node at given index"""
        if index < 0:
            raise SLLException
        current_node = self._head.next
        previous_node = self._head
        for i in range(index):
            previous_node = current_node
            if previous_node is None:
                raise SLLException
            current_node = current_node.next

        insert_val = SLNode(value)
        insert_val.next = previous_node.next
        previous_node.next = insert_val

    def remove_at_index(self, index: int) -> None:
        """removes node at given index"""
        if index < 0:
            raise SLLException
        current_node = self._head.next
        previous_node = self._head
        for i in range(index):
            if current_node is None:
                raise SLLException
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            raise SLLException
        previous_node.next = current_node.next
        current_node = current_node.next

    def remove(self, value: object) -> bool:
        """removes first instance of given value and returns true and otherwise false"""
        current_node = self._head.next
        previous_node = self._head
        for i in range(self.length()):
            if current_node.value == value:
                previous_node.next = current_node.next
                current_node = current_node.next
                return True
            previous_node = current_node
            current_node = current_node.next
        return False

    def count(self, value: object) -> int:
        """returns count of given value"""
        count = 0
        current_node = self._head.next
        for i in range(self.length()):
            if current_node.value == value:
                count += 1
            current_node = current_node.next
        return count

    def find(self, value: object) -> bool:
        """returns true if value is in linkedlist and false otherwise"""
        current_node = self._head.next
        for i in range(self.length()):
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """slices linkedlist at given index and creates a new linked list at value up to given size"""
        if start_index < 0 or size > self.length():
            raise SLLException
        new_linkedlist = LinkedList()
        current_node = self._head.next
        count = 0
        for i in range(self.length()):
            if i >= start_index and count < size:
                new_linkedlist.insert_back(current_node.value)
                count += 1
                if current_node.next is None and count < size:
                    raise SLLException
            current_node = current_node.next
        return new_linkedlist

if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
