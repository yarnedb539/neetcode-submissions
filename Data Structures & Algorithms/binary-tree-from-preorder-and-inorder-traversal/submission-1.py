class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        j = 0                                  # pointer into inorder

        for v in preorder[1:]:
            node = TreeNode(v)
            parent = None
            # pop while the stack top is the next node inorder finishes
            while stack and stack[-1].val == inorder[j]:
                parent = stack.pop()
                j += 1
            if parent:
                parent.right = node            # we just closed parent's left side
            else:
                stack[-1].left = node          # still going down-left
            stack.append(node)

        return root