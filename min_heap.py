# Course: CS261 - Data Structures
# Assignment: 5
# Student: Jordan Hendricks
# Description: Includes a min heap data structure


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """Adds a new value to min heap"""
        length = self.heap.length()
        current_index = length
        if self.heap.length() == 0:  # determines if the node is the first in the heap
            self.heap.append(node)
            return
        self.heap.append(node)  # appends node to end of list

        while current_index != 0:
            parent_index = int((current_index - 1) / 2)  # calculates the parent index
            parent = self.heap.get_at_index(parent_index)  # saves value of the parent
            if parent > node:
                temp_parent = parent_index  # temp variable to hold the parent's index during the swap
                parent_index = current_index
                current_index = temp_parent
                self.heap.set_at_index(parent_index, parent)  # swaps the parent and insertion values
                self.heap.set_at_index(current_index, node)
            else:
                return

    def get_min(self) -> object:
        """Returns the minimum element of the heap """
        if self.heap.length() == 0:
            raise MinHeapException
        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """Removes minimum element in the heap"""
        if self.heap.length() == 0:
            raise MinHeapException
        first = self.heap.get_at_index(0)
        last = self.heap.pop()
        length = self.heap.length()

        if length != 0:
            parent_index = 0  # sets the initial parent index
            self.heap.set_at_index(parent_index, last)

            while True:
                parent = self.heap.get_at_index(parent_index)  # saves value of the parent

                child_left_index = int((2 * parent_index) + 1)
                child_right_index = int((2 * parent_index) + 2)

                if length == 2:
                    child_left = self.heap.get_at_index(1)
                    if parent > child_left:
                        temp_parent_index = parent_index  # temp variable to hold the parent's index during the swap
                        parent_index = child_left_index
                        child_left_index = temp_parent_index
                        self.heap.set_at_index(parent_index, parent)  # swaps the parent and child values
                        self.heap.set_at_index(child_left_index, child_left)
                        return first

                if child_right_index >= length and child_left_index >= length:
                    return first

                elif child_right_index >= length:
                    child_left = self.heap.get_at_index(child_left_index)
                    min_child = child_left
                    min_child_index = child_left_index
                else:
                    child_left = self.heap.get_at_index(child_left_index)
                    child_right = self.heap.get_at_index(child_right_index)

                    if child_left <= child_right:
                        min_child = child_left
                        min_child_index = child_left_index
                    else:
                        min_child = child_right
                        min_child_index = child_right_index

                if parent > min_child:
                    temp_parent_index = parent_index  # temp variable to hold the parent's index during the swap
                    parent_index = min_child_index
                    min_child_index = temp_parent_index
                    self.heap.set_at_index(parent_index, parent)  # swaps the parent and child values
                    self.heap.set_at_index(min_child_index, min_child)

                else:
                    return first
        else:
            return first

    def build_heap(self, da: DynamicArray) -> None:
        """Builds a heap from an unsorted array"""
        length = da.length()
        self.heap = DynamicArray()
        for i in range(length):
            x = da.get_at_index(i)
            self.heap.append(x)

        start_index = int((length / 2) - 1)
        for index in range(start_index, -1, -1):
            self.build_heap_helper(index, length)

    def build_heap_helper(self, index, length):
        """Recursively builds the heap from an unsorted array"""
        min_index = index  # initializes the min index
        child_left_index = (2 * index) + 1
        child_right_index = (2 * index) + 2

        if child_left_index < length and self.heap.get_at_index(child_left_index) < self.heap.get_at_index(min_index):
            min_index = child_left_index

        if child_right_index < length and self.heap.get_at_index(child_right_index) < self.heap.get_at_index(min_index):
            min_index = child_right_index

        if min_index != index:
            self.heap.swap(index, min_index)
            self.build_heap_helper(min_index, length)

# BASIC TESTING
# if __name__ == '__main__':
    # print("\nPDF - add example 1")
    # print("-------------------")
    # h = MinHeap()
    # print(h, h.is_empty())
    # for value in range(300, 200, -15):
    #     h.add(value)
    #     print(h)

    # print("\nPDF - add example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)

    # print("\nPDF - get_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())

    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())

    # print("\nPDF - build_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)
    #
    # print("\n")

    # da = DynamicArray([-809, -189, 122, 959, -401, -609, 169, 205, -463, -496, 886, -67, -334, 827, 704, 251, -904, 120, 915, 355, -296, -758, 676, 405, -461, 707, -491, -66, -376, 467, 120, 761, -563, 434, 876, 760, 222, 722, 828, -660, -108, 796, -126, 147, -358, -840, 650, -136, -182, -831, -533, -406, -791, 435, -72, 266, -939, 395, 963, -890, 706, -469, 583, -493, 707, -394, 416])
    # # da = DynamicArray([500, 2, 11, 8, 6, 20, 1, 3, 7])
    # h = MinHeap([1, 1, 1, 1, 11, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    # print(h)
    # h.build_heap(da)
    # print(h)
    # print(da)
