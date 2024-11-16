class Solution(object):
    def longestZigZag(self, root):
        if not root:
            return 0

        stack = [(root, 0, 0)]
        maxi = 0

        while stack:
            node, left, right = stack.pop()
            maxi = max(maxi, left, right)

            if node.left:
                stack.append((node.left, right + 1, 0))

            if node.right:
                stack.append((node.right, 0, left + 1))

        return maxi