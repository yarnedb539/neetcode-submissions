class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split(","))
        def dfs():
            v = next(vals)
            if v == "N":
                return None
            node = TreeNode(int(v))
            node.left = dfs()       # same order as serialize: node, left, right
            node.right = dfs()
            return node
        return dfs()