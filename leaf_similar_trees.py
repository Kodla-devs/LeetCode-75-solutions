class Solution(object):
    def leafSimilar(self, root1, root2):
        
        def get_leaves(root):
            leaves = []
            
            def dfs(node):
                if node:
                    if not node.left and not node.right:
                        leaves.append(node.val)
                    dfs(node.left)
                    dfs(node.right)
            dfs(root)
            return leaves

        return get_leaves(root1) == get_leaves(root2)