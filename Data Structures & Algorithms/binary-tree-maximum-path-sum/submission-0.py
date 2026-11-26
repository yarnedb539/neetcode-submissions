class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = root.val                          # not 0: all-negative trees exist

        def gain(node):
            nonlocal best
            if not node:
                return 0
            left = max(gain(node.left), 0)       # drop negative branches
            right = max(gain(node.right), 0)
            best = max(best, node.val + left + right)   # path bending here
            return node.val + max(left, right)          # one branch only, upward

        gain(root)
        return best