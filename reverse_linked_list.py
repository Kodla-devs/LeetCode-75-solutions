class Solution(object):
    def reverseList(self, head):
        ref = None
        current = head

        while current:
            next_node = current.next
            current.next = ref
            ref = current
            current = next_node

        return ref