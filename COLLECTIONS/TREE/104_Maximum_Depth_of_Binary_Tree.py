"""104. Maximum Depth of Binary Tree"""


class TreeNode:

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode" = None,
        right: "TreeNode" = None,
    ):
        self.val = val
        self.right = right
        self.left = left


class Solution(object):

    def maxDepth_recursion(self, root: TreeNode) -> int:
        """нахождение максимальной глубины DFS через рекурсию"""
        if not root:
            return 0
        return 1 + max(
            self.maxDepth_recursion(root.left), self.maxDepth_recursion(root.right)
        )

    def maxDepth(self, root: TreeNode):
        """нахождение максимальной глубины DFS через список и цикл"""

        queue = [(root, 1)]

        max_depth = 0

        while queue:
            node, depth = queue.pop(-1)

            right = node.right
            left = node.left

            max_depth = depth if depth > max_depth else max_depth

            if right:
                queue.append((right, depth + 1))
            if left:
                queue.append((left, depth + 1))


if __name__ == "__main__":
    print("")
