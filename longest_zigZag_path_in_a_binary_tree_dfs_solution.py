class Solution(object):
    def longestZigZag(self, root):
        self.maxi = 0

        def dfs(node, left, right):
            self.maxi = max(self.maxi, left, right)

            if node.left:
                dfs(node.left, right + 1, 0)
            
            if node.right:
                dfs(node.right, 0, left + 1)
        
        dfs(root, 0, 0)
        return self.maxi