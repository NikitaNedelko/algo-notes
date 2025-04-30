"""
98. Validate Binary Search Tree
Учитывая root двоичного дерева, определите, является ли оно допустимым двоичным деревом поиска (BST).

Действительный BST определяется следующим образом:

Левое поддерево узла содержит только узлы с ключами, меньшими, чем ключ узла.
Правое поддерево узла содержит только узлы с ключами, большими, чем ключ узла.
И левое, и правое поддеревья также должны быть бинарными деревьями поиска.

какие передаваемые данные нв вход
что вывести надо ?
"""

from typing import Optional


class TreeNode(object):
    def __init__(
        self,
        val: int = 0,
        right: Optional["TreeNode"] = None,
        left: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def isValidBST(self, root: Optional["TreeNode"]) -> bool:

        min_val = float("-inf")
        max_val = float("inf")

        stack = [(root, min_val, max_val)]

        while stack:
            node, min_val, max_val = stack.pop(-1)

            if not node:
                continue

            node_val = node.val

            if not (min_val < node_val < max_val):
                return False

            node_right = node.right
            node_left = node.left

            if node_right:
                stack.append((node_right, node_val, max_val))

            if node_left:
                stack.append((node_left, min_val, node_val))

        return True
