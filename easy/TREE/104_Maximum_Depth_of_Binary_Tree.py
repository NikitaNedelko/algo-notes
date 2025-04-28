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

    def maxDepth(self, root: TreeNode):
        """нахождение максимальной глубины DFS через рекурсию"""

        queue = [root]

        while queue:
            node = queue.pop(-1)

            queue.append(node.right)


if __name__ == "__main__":
    print("")
