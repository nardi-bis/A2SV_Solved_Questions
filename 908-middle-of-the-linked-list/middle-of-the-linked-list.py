# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head # slow one(first)
        j = head # fast one(second)

        while j is not None and j.next is not None:
            i = i.next
            j = j.next.next

        return i