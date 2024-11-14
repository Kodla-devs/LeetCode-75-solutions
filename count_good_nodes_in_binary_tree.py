class Solution(object):
    def goodNodes(self, root):

        def dfs(node, max_val):
            if not node:
                return 0
            
            good = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            return good + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, root.val)