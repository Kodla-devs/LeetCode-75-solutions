class Solution(object):
    def reverseList(self, head):
        # listeyi tersine cevir
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
    
    def pairSum(self, head):
        # ortancayı bul
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reverseList(slow)

        # maximum toplamı hesapla
        max_sum = 0
        first_half = head
        while second_half:
            twin_sum = first_half.val + second_half.val
            max_sum = max(max_sum, twin_sum)
            first_half = first_half.next
            second_half = second_half.next

        return max_sum