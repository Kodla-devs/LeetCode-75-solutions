from collections import deque


class Solution(object):
    def maxLevelSum(self, root):
        if not root:
            return 0
        
        queue = deque([root])
        max_sum = root.val
        max_level = 1
        current_level = 0

        while queue:
            current_level += 1
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
        
        return max_level