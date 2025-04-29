"""110. Balanced Binary Tree"""

# Definition for a binary tree node.

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
    def isBalanced(self, root: Optional[TreeNode]):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        self.flag = True

        def rec(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left = rec(root.left)
            right = rec(root.right)
            if abs(left - right) > 1:
                self.flag = False
                return 0
            return 1 + max(left, right)

        rec(root)

        return self.flag
