# Course: CS261 - Data Structures
# Assignment: 5
# Student: Jordan Hendricks
# Description:


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

        parent_index = int((length - 2) / 2)
        switch = False

        self.build_heap_helper(parent_index, length, switch)

    def build_heap_helper(self, parent_index, length, switch):
        """"""
        if parent_index == -1:
            return
        parent = self.heap.get_at_index(parent_index)
        child_left_index = int((2 * parent_index) + 1)
        child_right_index = int((2 * parent_index) + 2)

        if child_right_index >= length and child_left_index >= length:
            return

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

            if switch is True:
                self.build_heap_helper(parent_index, length, True)
                return
            self.build_heap_helper(temp_parent_index - 1, length, False)

        else:
            parent_index -= 1
            if switch is True:
                return
            self.build_heap_helper(parent_index, length, False)


# BASIC TESTING
if __name__ == '__main__':
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

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)

    print("\n")

    da = DynamicArray([-948, -231, 174, 262, -862, -869, 552, -395, 398, 538, -442, -530, 822, 327, -802, -117, 723, 818, -526, 440, -658, 308, 651, 441, 627, -5, -306, 317, 498, 245, -630, 669, -97, -442, -574, -129, -758, 665, 143, -897, 436, -807, 457, -360, 472, -55, -512, 149, -638, -923, 527, 859, 662, 614, -183, -967, 257, 769, 723, 955, -729, 392, 978, 844, 252, -258, -809, 474, 787, -509, 305, 437, 851, -702, 812, 379, -611, -7, -712, 250, -64, -230, -676, 396, -525, -763, -220, 717, 527, 597, 691, -806, 62, -275, -639, 914, -812, -960, 313, 887, 938, -693, -540, 549, 32, -241, -88, -865, -186, -397, -439, -770, -282, 687, 168, -932, 262, 214, 835, -912, -586, 509, 876, -178, -382, -367, -577, -539, -181, -34, -42, -405, 21, -468, 912, 967, 647, 362, -149, 511, 60, 416, -514, 169, 920, 591, 957, 96, -693, -293, 274, 97, 285, 666, -622, 930, 107, -902, -788, -736, 548, 630, -982, -677, -771, -144, -679, 126, 53, -956, -53, 562, 582, 382, 815, -710, -208, 41, -900, -949, 612, -315, 643, -994, -333, -655, -228, -178, 959, 811, -267, -737, -181, 74, -597, -661, 34, -871, 262, -560, 399, -150, 231, 423, 267, 885, 616, -930, 797, -462, 630, 368, -849, -47, -998, -238, 969, 993, 50, -521, 554, -867, -701, -49, 905, -24, 383, 649, 727, 449, -575, 25, -756, -768, 466, 786, -955, -877, -984, 290, 565, 543, -592, 486, 513, 813, -52, 395, 261, -32, -279, -106, -203, 280, -189, -2, -927, 682, -15, 154, 535, -352, 2, 132, -97, 721, -239, -510, -702, 706, -304, -286, -545, 300, 762, -96, -100, -813, 192, 755, 836, -618, -126, -317, -263, 444, -208, 305, -518, 163, 930, -795, 836, -312, -533, 777, -149, 904, -676, 594, -586, -163, -83, -457, -569, 826, 420, 624, -24, 138, -561, 976, 712, 75, 76, 725, -464, 845, -830, -454, -57, -844, 36, 175, 179, 644, 894, 966, 151, 132, -994, 811, 970, 621, 120, -290, -128, 769, -975, 259, -193, -192, 833, 537, -961, 245, 320, -308, 101, 314, -214, 508, -855, -625, 700, -945, -564, 803, -866, -193, -593, -333, 953, -560, -53, 987, 948, -390, 673, 487, 419, 630, 405, -756, 643, 997, -220, -922, 263, 66, -521, -501, 469, 270, -617, 223, -988, 757, -341, 296, 466, -793, 594, -712, -224, 485, -460, -521, -677, 179, -966, -711, -883, 544, 299, -684, -457, -572, 459, 93, -231, 36, -258, -547, -264, -992, 295, -600, -693, -591, 881, 511, -479, -324, 736, -74, -643, -578, 317, 412, -968, -639, -652, -705, -671, -453, -665, -744, 101, 35, 737, 123, 568, -459, 838, 732, -242, -17, 246, 381, -726, 399, 119, 598, -199, -109, 631, 877, 729, -597, 317, 363, -239, 674, 366, -162, 322, 880, -201, 523, -742, 874, 186, 697, -251, -516, 832, -743, -177, 859, 90, -427, -572, -633, 682, 489, -102, 922, 25, -617, -160, -678, 755, 475, 25, 640, 409, -395, 8, -685, 299, 236, -399, 101, 290, -147, -255, -961, 283, -371, -221, -451, 38, -639, -229, 781, 701, 277, 874, 166, -904, 48, 975, 55, -9, 474, -463, -465, -448, 365, 872, 585, 696, 730, -5, -475, -184, 101, 76, 668, -436, -846, -874, -729, 148, -355, -898, -761, 353, -770, -918, -338, 821, -811, -733, -495, 948, 967, -134, -61, -156, -493, -13, -605, -1, -830, -117, 201, 839, 302, 197, -197, 109, 932, -298, 387, -324, 565, 883, -343, 149, -978, 701, -910, 203, -566, 964, 622, -735, -362, -469, -3, 175, -591, 40, -706, 776, -308, 596, 388, -328, 810, 134, 29, 133, 101, -253, 439, 25, 170, -964, 280, 673, -336, 591, 809, -164, -669, 320, -657, -566, 887, -547, -368, -225, 310, 197, -346, 476, -133, 533, -898, 79, -564, -885, -892, -542, -555, 158, -432, -728, -690, 341, 695, 703, -395, -782, -917, -909, 14, 210, -72, -827, 704, -351, 964, 472, -404, -730, -176, 68, 658, -21, 806, -370, 157, -531, -229, 85, -641, 188, -508, -140, 388, 963, 372, 823, 910, 400, 360, 749, 442, -519, -935, 418, 455, 150, 137, 543, -90, 930, 358, -267, 246, -787, 340, 165, 831, -914, 313, -856, -334, -1, 829, 264, -811, -760, 261, -356, -295, -907, -382, -329, 438, -317, 843, -191, 319, -339, 231, -135, 906, 763, -280, -222, -479, -299, 425, 451, -140, -57, -426, -567, -540, -13, 735, 295, 476, -216, -171, -290, 802, 956, -147, 513, 592, -899, -453, 427, 528, -161, 844, 931, 269, -989, -777, 21, 512, 87, -419, 957, -202, 525, 896, -295, 239, -424, -609, -297, 27, 709, 931, 387, -930, 710, 533, -227, 902, -68, -729, -494, 691, 376, -221, -664, 248, 698, 949, -772, 843, 321, 670, 860, 236, 853, 329, -357, 142, 431, 419, 243, -831, -743, -915, 361, 58, 127, 716, -145, -1, 632, -700, -663, 687, -36, 698, 552, 661, 484, 122, -824, 335, 150, -457, 909, -179, -160, 657, 608, -936, 159, -103, -65, 396, -815, 326, 796, 45, 233, 468, -780, 400, -787, -824, 849, 953, -38, -495, 615, -689, -941, -125, 407, 590, -504, 244, 562, -334, -989, 936, 723, -339, -869, 995, 422, 554, -7, -50, 862, -581, 834, -809, 239, -23, -358, -391, -120, -507, -300, -67, 877, -376, -858, 693, 688, -107, -776, -136, -465, -388, -840, 465, 919, 599, -119, -255, 312, -125, -544, 670, -899, -819, 756, 883, 899, 455, -826, 511, 251, 904, 517, -649, -234, -223, 257, 559, -862, 319, -568, 550, 450, -367, 349, 316, 766, 37, -263, 718, -204, 845, 185, -334, 221, 219, -803, -676, 374, -884, 644, 74, 225, 891, 563, 232, 949, 926, -182, -968, 265, -984, 696, -281])\
    # da = DynamicArray([500, 2, 11, 8, 6, 20, 1, 3, 7])
    h = MinHeap([1, 1, 1, 1, 11, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    print(h)
    h.build_heap(da)
    print(h)
    # print(da)
