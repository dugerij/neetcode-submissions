# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        past = head
        future = head
        

        while future and future.next:
            past = past.next
            future = future.next.next

            if past == future:
                return True

        return False