class Solution(object):
    def searchBST(self, root, val):

        if not root:
            return None

        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        
        return self.searchBST(root.right, val)