"""100. Same Tree"""

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
    def isSameTree(self, p: Optional[TreeNode], q:Optional[TreeNode]):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        q_tree = [q]
        p_tree = [p]

        while q_tree and p_tree:

            q_node = q_tree.pop(0)
            p_node = p_tree.pop(0)

            if q_node is p_node is None:
                continue
        elif:

            if q_node.val != p_node.val:
                return False

            q_tree.append(q_node.left)
            q_tree.append(q_node.right)

            p_tree.append(p_node.left)
            p_tree.append(p_node.right)

        return True
