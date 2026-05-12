# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def mergetwolists(
        self, list1: Optional[ListNode], list2: Optional[listNode]
        ) -> Optional[ListNode]:

        merged = ListNode()
        current = merged

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        current.next = list1 if list1 else list2

        return merged.next 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        merged_list = lists[0] 

        for i in range(1, len(lists)):
            merged_list = self.mergetwolists(
                list1=merged_list,
                list2=lists[i]
            )

        return merged_list

        
