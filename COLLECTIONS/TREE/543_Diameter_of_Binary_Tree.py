"""543. Diameter of Binary Tree"""

from typing import Optional


class TreeNode(object):
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root: TreeNode):
        """Обход через DFS"""

        self.max_diameter: int = 0

        def rec(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = rec(node.left)
            right = rec(node.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)

        rec(root)

        return self.max_diameter
