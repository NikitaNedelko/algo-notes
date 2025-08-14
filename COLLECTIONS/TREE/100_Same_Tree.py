"""100. Same Tree"""

from typing import Optional
from collections import deque


# class TreeNode(object):

#     def __init__(
#         self,
#         val: int = 0,
#         left: Optional["TreeNode"] = None,
#         right: Optional["TreeNode"] = None,
#     ):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution(object):
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
#         """
#         :type p: Optional[TreeNode]
#         :type q: Optional[TreeNode]
#         :rtype: bool
#         """

#         q_tree = [q]
#         p_tree = [p]

#         while q_tree and p_tree:

#             q_node = q_tree.pop(0)
#             p_node = p_tree.pop(0)

#             if q_node is p_node is None:
#                 continue

#             if q_node.val != p_node.val:
#                 return False

#             q_tree.append(q_node.left)
#             q_tree.append(q_node.right)

#             p_tree.append(p_node.left)
#             p_tree.append(p_node.right)

#         return True


class TreeNode(object):
    def __init__(self, val: int, right: "TreeNode", left: "TreeNode") -> None:
        self.val = val
        self.right = right
        self.left = left


class Solution(object):
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        q_tree = [p]
        p_tree = [q]

        while p_tree or q_tree:
            node_p = p_tree.pop(-1)
            node_q = q_tree.pop(-1)

            if node_p is node_q is None:
                continue

            if node_p.val != node_q.val:
                return False

            q_tree.append(node_q.right)
            q_tree.append(node_q.left)

            p_tree.append(node_p.right)
            p_tree.append(node_p.left)

        return True
