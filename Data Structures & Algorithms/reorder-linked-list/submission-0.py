# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverselist(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second = slow.next
        slow.next = None

        second = self.reverselist(second)

        merged = head
        
        while second:
            tmp1 = merged.next
            tmp2 = second.next

            merged.next = second
            second.next = tmp1

            merged = tmp1
            second=tmp2