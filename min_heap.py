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

        # parent_index = int((length - 2) / 2)
        for index in range(int(length/2), -1, -1):
            self.build_heap_helper(index, length)

        # switch = False

        # self.build_heap_helper(parent_index, length, switch)

    # def build_heap_helper(self, parent_index, length, switch):
    #     """"""
    #     if parent_index == -1:
    #         return
    #     parent = self.heap.get_at_index(parent_index)
    #     child_left_index = int((2 * parent_index) + 1)
    #     child_right_index = int((2 * parent_index) + 2)
    #
    #     if child_right_index >= length and child_left_index >= length:
    #         return
    #
    #     elif child_right_index >= length:
    #         child_left = self.heap.get_at_index(child_left_index)
    #         min_child = child_left
    #         min_child_index = child_left_index
    #     else:
    #         child_left = self.heap.get_at_index(child_left_index)
    #         child_right = self.heap.get_at_index(child_right_index)
    #
    #         if child_left <= child_right:
    #             min_child = child_left
    #             min_child_index = child_left_index
    #         else:
    #             min_child = child_right
    #             min_child_index = child_right_index
    #
    #     if parent > min_child:
    #         temp_parent_index = parent_index  # temp variable to hold the parent's index during the swap
    #         parent_index = min_child_index
    #         min_child_index = temp_parent_index
    #         self.heap.set_at_index(parent_index, parent)  # swaps the parent and child values
    #         self.heap.set_at_index(min_child_index, min_child)
    #
    #         if switch is True:
    #             self.build_heap_helper(parent_index, length, True)
    #             return
    #         self.build_heap_helper(temp_parent_index - 1, length, False)
    #         return
    #
    #     else:
    #         parent_index -= 1
    #         self.build_heap_helper(parent_index, length, False)

    def build_heap_helper(self, index, length):
        """Recursively builds a heap from an unorganized list"""
        leaf = False
        if index >= int(length/2) and index <= length:
            leaf = True

        parent = self.heap.get_at_index(index)
        child_left_index = int((2 * index))
        child_right_index = int((2 * index) + 1)

        if not leaf:
            left_child = self.heap.get_at_index(child_left_index)
            right_child = self.heap.get_at_index(child_right_index)
            if parent > left_child or parent > right_child:

                if left_child < right_child:
                    self.heap.swap(index, child_left_index)
                    self.build_heap_helper(child_left_index, length)

                else:
                    self.heap.swap(index, child_right_index)
                    self.build_heap_helper(child_right_index, length)



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

    da = DynamicArray([-784, -83, -860, -628, 596, 821, -453, 375, 402, -298, -44, 851, 271, 944, 295, 954, 533, -965, 883, 721, -46, 47, -625, -317, 890, 533, -765, -276, 958, 899, 148, 358, 365, 339, -554, -111, -390, 94, -134, -217, 252, 547, -757, -809, 660, -607, 188, -119, -175, 581, -134, 659, -237, 993, 39, 848, 904, -729, 273, 151, -558, -232, 308, 579, -523, 618, -279, 988, 854, 934, -146, 124, -543, 874, -419, 920, -702, 33, 705, 963, 951, 743, 364, 32, -979, 842, -119, 819, 430, -854, 531, -486, -68, 184, 526, -328, 842, -889, -196, 465, -224, 367, -512, 631, -217, 956, -174, 982, -332, -209, -786, -997, -225, 222, 330, -202, -535, 702, 490, 759, 787, 269, 172, 100, 386, 652, 196, 342, 635, 629, 959, 611, -10, -602, 592, -628, 910, 504, -945, 545, -123, -25, -251, -532, -774, 204, 525, 231, 363, -865, 965, -410, 216, -629, 570, -89, 286, -824, 212, 400, -5, -181, 135, -683, -778, -396, -80, 770, -140, 68, 512, 415, 340, -189, 516, 598, 753, 910, -83, -344, 839, 834, 30, -695, -200, -952, 898, 146, 750, -790, -5, -804, -748, 480, -24, -108, -404, 835, -42, -108, 431, -853, -309, -92, -512, 90, 264, 218, 826, -307, 640, 568, -646, 633, 689, 178, -217, 34, 579, -262, -637, 490, 321, 63, 978, 78, -314, -348, 525, -151, -88, -766, 303, 578, -834, -779, -257, -243, 161, -761, 512, -903, 554, -781, 970, 942, 850, -393, -183, -350, -755, 787, -851, -79, 756, -818, -494, 116, 469, 254, 470, -789, -516, 880, -245, 276, -438, 99, -187, -683, 224, -537, 876, -661, 60, -744, 321, 575, 163, -629, 290, 281, 69, -833, -481, -313, -524, 863, -119, 978, -755, -34, -897, -845, 135, 544, -66, -863, 474, 674, 15, -902, -72, 966, 965, -109, 227, -127, -151, -71, 122, 765, 368, 330, -164, -859, -11, 328, -630, -605, 239, 838, 683, 826, 101, 939, 800, 205, 142, -663, -587, -898, -79, 799, 780, 704, 927, -533, 121, 168, -927, 232, -332, -387, 289, 46, -316, -701, -394, -426, 178, 730, 127, 855, 766, -937, 191, -251, -670, -71, -239, -472, 211, 550, 469, 39, -712, 16, 233, -456, -777, -300, 325, -522, -360, -220, -343, -75, -859, -821, -381, 704, -709, -253, 932, -686, 417, 0, -780, 377, -998, -357, -893, 907, 155, -77, 116, 902, 848, 512, 566, -365, 53, -775, -916, -437, -828, -325, 979, 434, 478, 738, 291, 310, 459, -723, 192, -757, 420, -874, 554, -77, -969, -79, 248, 198, -120, 253, -398, -167, 68, -742, 13, 676, 290, 494, -322, 148, 633, 257, 632, 129, -952, 388, -241, -697, 298, 247, -437, -382, 580, -190, -751, -232, 103, 405, -804, 500, 468, -281, -384, 517, 296, -677, 273, -823, -766, -82, -183, 898, -194, -516, 475, -843, -792, 522, 35, 118, -732, 890, -407, -300, -129, 242, 489, -490, -771, -62, 631, 847, 5, 287, 418, -640, 476, -623, 295, -253, -111, 680, -575, 293, 99, 637, 172, 609, -191, -135, 177, -121, 667, 142, 502, 616, -233, 309, -535, 170, 357, -64, 65, -365, 396, 931, 730, -414, 932, 496, 830, 991, 527, -237, -904, -279, -625, -644, -382, -930, 56, 455, -405, 119, -138, -937, -795, -685, 138, -285, -812, -288, 404, -567, 43, 104, 842, -260, -428, 411, 865, -531, -18, 44, 686, 734, 962, 947, 868, 329, 358, -615, -501, 90, 394, 172, -466, 302, 944, -351, 962, -324, -517, 123, -685, 973, 218, -108, 683, 968, 346, -245, 290, 897, -349, -112, 920, 350, 964, 55, -101, -459, -9, -377, -308, 603, -109, -526, -958, 347, 473, 317, -964, -510, -125, -475, -785, 668, -573, 583, -433, -751, 500, -524, -270, 30, 917, -495, -5, -308, -518, 578, -985, -811, -767, 663, 857, 300, 85, -122, 668, -81, -724, -718, -226, 95, -359, 917, -83, -664, -236, -916, -148, 276, 122, -295, -816, -732, -857, -185, 244, -376, 488, 310, 961, -277, 217, 114, -364, -466, 2, 396, -485, 792, -550, 822, -644, -430, 331, 789, -805, 786, -753, -204, -759, 733, -819, -205, -859, -162, -372, 624, -164, 287, 55, 818, -793, -897, 230, -599, -814, 72, 414, -697, 951, 329, 447, 947, -154, -644, -445, -281, -722, -125, 152, -917, 203, 871, 939, -593, -849, -206, -400, 1, -226, -482, -396, 424, 876, -579, -612, 432, 831, -730, 837, 575, -587, 268, -656, -267, -599, -523, 713, 616, -792, -881, 734, 237, 789, -405, 699, -830, -451, -88, 43, 446, -98, -270, 147, -968, 672, -9, -412, 68, -337, -988, 623, -324, 930, 822, 163, 576, -23, 164, 490, 255, -612, 225, -75, 7, 447, -389, 913, 803, -308, -691, -23, 430, 383, 791, 804, 15, -201, -978, 298, -496, 298, -9, -264, -784, 58, 598, -91, 328, -761, -425, -35, -787, 515, -834, 467, -550, -446, -615, 235, -23, -974, 195, 350, -176, 960, -973, 614, 48, 937, -405, -151, -107, 210, 300, -516, 873, -338, -527, -518, -425, -464, -372, 607, -258, 822, 41, 669, 703, -378, 139, -250, 931])
    # da = DynamicArray([500, 2, 11, 8, 6, 20, 1, 3, 7])
    h = MinHeap([1, 1, 1, 1, 11, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    print(h)
    h.build_heap(da)
    print(h)
    # print(da)
