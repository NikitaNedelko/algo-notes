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
