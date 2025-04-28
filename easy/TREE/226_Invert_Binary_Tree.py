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

    def invert(self, node: Optional[TreeNode]):
        if node is None:
            return None
        node.left, node.right = node.right, node.left
        self.invert(node.right)
        self.invert(node.left)
        return node

    def invertTree(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.invert(root)
        return root


if __name__ == "__main__":
    print("")

"""
1 2 4 5 6 7 9 10
2 8 12

1 2 4
1 3 4
"""
