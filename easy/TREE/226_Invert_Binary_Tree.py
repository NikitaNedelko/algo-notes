"""226. Invert Binary Tree

Скорость работы:
Затрачено памяти:
"""

from typing import Optional


class TreeNode(object):

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, nums: list[int]):
        self.root = None
        for num in nums:
            self.insert_rec(num)

    # def build_tree(self, nums: list[int]) -> Optional[TreeNode]:

    #     self.root = TreeNode(nums.pop(0) if nums else 0)

    #     queue = [self.root]

    #     while nums:
    #         node = queue.pop(0)
    #         val_left = nums.pop(0)
    #         val_right = nums.pop(0)

    #         if val_left:
    #             node.left = TreeNode(val_left)
    #             queue.append(node.left)
    #         if val_right:
    #             node.right = TreeNode(val_right)
    #             queue.append(node.right)

    def insert_rec(self, val: int):
        """Вставка значения через рекурсию"""

        def rec(node: Optional[TreeNode], val: int):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = rec(node.left, val)
            else:
                node.right = rec(node.right, val)

        self.root = rec(self.root, val)

    def insert(self, val: int):
        """Вставка значения без с помощью цикла"""

        new_node = TreeNode(val)

        if not self.root:
            self.root = new_node
            return

        current = self.root
        while True:
            if val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node

    def delete_rec(self, val: int):
        """Удаление значения через рекурсию"""

        def rec(node: Optional[TreeNode], val: int):
            if not node:
                return None
            if val < node.val:
                # ищем наш узел
                node.left = rec(node.left, val)
            elif val > node.val:
                # ищем наш узел
                node.right = rec(node.right, val)
            else:
                # узел найден

                # если у него нет хоть одного потомка,
                # то сразу возвращаем ссылку на ту ветку
                if not node.right:
                    return node.left
                if not node.left:
                    return node.right

                # если у узла 2 потомка,
                # то находим самое маленькое число в правой ветке и ставим его в node.val
                # затем запускаем рекурсию на ужаление этого числа node.right = rec(node.right, node.val)
                min_node = node.right

                while min_node.left:
                    min_node = min_node.left

                node.val = min_node.val
                node.right = rec(node.right, node.val)

            return node

        self.root = rec(self.root, val)


class Solution(object):

    def invert_recursion(self, node: Optional[TreeNode]):
        """Обход BFS через рекурсию"""
        if node is None:
            return None
        node.left, node.right = node.right, node.left
        self.invert_recursion(node.right)
        self.invert_recursion(node.left)
        return node

    def invert_queue(self, root: Optional[TreeNode]):
        """Обход BFS через очередь цикл"""
        if root is None:
            return None

        queue = [root]
        while queue:
            node = queue.pop(0)

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

    def invertTree(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.invert_queue(root)
        return root


if __name__ == "__main__":
    print("")
