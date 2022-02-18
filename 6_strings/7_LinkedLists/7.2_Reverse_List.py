class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head:
            prev = head
            head = head.next
            prev.next = None

        else:
            return head

        while head:
            nxt = head.next
            head.next = prev

            prev = head
            head = nxt

        return prev
