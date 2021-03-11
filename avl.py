# Course: CS261 - Data Structures
# Author: Jordan Hendricks
# Assignment: Assignment: 5
# Description: Includes a min heap data structure

import random

from bst import BST
from bst import TreeNode
from bst import Stack
from bst import Queue


class AVLTreeNode(TreeNode):
    """
    AVL Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        super().__init__(value)
        self.parent = None
        self.height = 0


class AVL(BST):
    def add(self, value):
        """Adds a new value to the tree"""
        node = AVLTreeNode(value)
        if self.root is None:
            self.root = node
            node.height = 1
            return

        current = self.root
        # height = 0
        # while current is not None:  # runs until the desired node is reached
        #     parent = current
        #     if value < current.value:
        #         height += 1
        #         if current.left is None:
        #             root = current
        #             node.height = height
        #             node.parent = parent
        #             break
        #         current = current.left
        #
        #     elif value >= current.value:
        #         if current.right is None:
        #             root = current
        #             node.height = height
        #             node.parent = parent
        #
        #             break
        #         current = current.right
        #
        # self.add_helper(root, node)

        height = 0
        # adds the node as a normal BST updating parent and height
        while current is not None:  # runs until the desired node is reached
            parent = current
            height += 1
            if value < current.value:
                if current.left is None:
                    current.left = node
                    node.parent = parent
                    node.height = height
                    break
                current = current.left

            elif value >= current.value:
                if current.right is None:
                    current.right = node
                    node.parent = parent
                    node.height = height
                    break
                current = current.right

        while current is not None:
            balance = self.balance_factor(current)
            if balance > 1:
                print(current)
                self.left_rotate(current)
                # print(current.parent)
                return


            current = current.parent

    # def add_helper(self, root, node):
    #     """Recursively adds a new node to the tree"""
    #     value = node.value
    #     if not root:
    #         return AVLTreeNode(value)
    #     elif value < root.value:
    #         root.left = self.add_helper(root.left, node)
    #     else:
    #         root.right = self.add_helper(root.right, node)
    #
    #     # root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
    #
    #     balance = self.balance_factor(root)
    #     if balance < -1 and value < root.left.value:
    #         print(True)
    #         return self.right_rotate(root)

    def left_rotate(self, node):
        """Performs a rotate left"""
        # node_parent = node.parent
        new_root = node.right  # determine the new root after the rotate
        right_left = new_root.left

        # changes pointers updates parents
        new_root.left = node  # the new root's right node becomes the old root node
        # new_root.parent = node_parent
        # node.parent = new_root

        node.right = right_left

        # if right_left is not None:
        #     right_left.parent = node

        new_root.height = 1 + max(self.get_height(new_root.right), self.get_height(new_root.left))
        node.height = 1 + max(self.get_height(node.right), self.get_height(node.left))

        # return new_root

    def right_rotate(self, node):
        """Performs a rotate right"""
        new_root = node.left  # determine the new root after the rotate
        left_right = new_root.right

        # changes pointers
        new_root.right = node  # the new root's right node becomes the old root node
        node.left = left_right

        new_root.height = 1 + max(self.get_height(new_root.right), self.get_height(new_root.left))
        node.height = 1 + max(self.get_height(node.right), self.get_height(node.left))

        return new_root

    def get_height(self, root) -> int:
        """Determines the height of the binary tree"""
        if not root:
            return 0
        return root.height
        # return self.get_height_helper(node)

    def get_height_helper(self, node):
        """Recursively goes through the binary tree to determine height"""
        if node is None:
            return -1

        left_height = self.height_helper(node.left)
        right_height = self.height_helper(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def balance_factor(self, root):
        """Returns the balance factor at a subtree root"""
        right_height = self.get_height(root.right)
        left_height = self.get_height(root.left)
        return right_height - left_height

    def remove(self, value) -> bool:
        """
        TODO: Write your implementation
        """
        pass


# if __name__ == '__main__':
#
#     print("\nPDF - method add() example 1")
#     print("----------------------------")
#     test_cases = (
#         (1, 2, 3),          #RR
#         (3, 2, 1),          #LL
#         (1, 3, 2),          #RL
#         (3, 1, 2),          #LR
#     )
#     for case in test_cases:
#         avl = AVL(case)
#         print(avl)


    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # test_cases = (
    #     (10, 20, 30, 40, 50),   # RR, RR
    #     (10, 30, 30, 50, 40),   # RR, RL
    #     (30, 20, 10, 5, 1),     # LL, LL
    #     (30, 20, 10, 1, 5),     # LL, LR
    #     (5, 4, 6, 3, 7, 2, 8),  # LL, RR
    #     (range(0, 30, 3)),
    #     (range(0, 31, 3)),
    #     (range(0, 34, 3)),
    #     (range(10, -10, -2)),
    #     ('A', 'B', 'C', 'D', 'E'),
    #     (1, 1, 1, 1),
    # )
    # for case in test_cases:
    #     avl = AVL(case)
    #     print('INPUT  :', case)
    #     print('RESULT :', avl)


    # print("\nPDF - method remove() example 1")
    # print("-------------------------------")
    # test_cases = (
    #     ((1, 2, 3), 1),                             # no AVL rotation
    #     ((1, 2, 3), 2),                             # no AVL rotation
    #     ((1, 2, 3), 3),                             # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 0),
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 45),     # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 40),     # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 30),     # no AVL rotation
    # )
    # for tree, del_value in test_cases:
    #     avl = AVL(tree)
    #     print('INPUT  :', avl, "DEL:", del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)


    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # test_cases = (
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 20),     # RR
    #     ((50, 40, 60, 30, 70, 20, 80, 15), 40),     # LL
    #     ((50, 40, 60, 30, 70, 20, 80, 35), 20),     # RL
    #     ((50, 40, 60, 30, 70, 20, 80, 25), 40),     # LR
    # )
    # for tree, del_value in test_cases:
    #     avl = AVL(tree)
    #     print('INPUT  :', avl, "DEL:", del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)


    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # case = range(-9, 16, 2)
    # avl = AVL(case)
    # for del_value in case:
    #     print('INPUT  :', avl, del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)


    # print("\nPDF - method remove() example 4")
    # print("-------------------------------")
    # case = range(0, 34, 3)
    # avl = AVL(case)
    # for _ in case[:-2]:
    #     print('INPUT  :', avl.size(), avl, avl.root)
    #     avl.remove(avl.root.value)
    #     print('RESULT :', avl)


    # print("\nPDF - method remove() example 5")
    # print("-------------------------------")
    # for _ in range(100):
    #     case = list(set(random.randrange(1, 20000) for _ in range(900)))
    #     avl = AVL(case)
    #     if avl.size() != len(case):
    #         raise Exception("PROBLEM WITH ADD OPERATION")
    #     for value in case[::2]:
    #         avl.remove(value)
    #     if avl.size() != len(case) - len(case[::2]):
    #         raise Exception("PROBLEM WITH REMOVE OPERATION")
    # print('Stress test finished')


    # """ Comprehensive example 1 """
    # print("\nComprehensive example 1")
    # print("-----------------------")
    # tree = AVL()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'  N/A {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')
    #
    # for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print()
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())


    # """ Comprehensive example 2 """
    # print("\nComprehensive example 2")
    # print("-----------------------")
    # tree = AVL()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'N/A   {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')
    #
    # for value in 'DATA STRUCTURES':
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print('', tree.pre_order_traversal(), tree.in_order_traversal(),
    #       tree.post_order_traversal(), tree.by_level_traversal(),
    #       sep='\n')
