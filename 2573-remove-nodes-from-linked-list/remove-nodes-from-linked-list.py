# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        stack = []
        while cur:
            while stack and cur.val > stack[-1] :
                stack.pop()
            stack.append(cur.val)
            cur = cur.next
    # building a linked list from a stack(list)

        new = ListNode(0) #dummy node
        current = new # now cuurent points to the dummy node '
        for x in stack:
            current.next = ListNode(x)
            current = current.next
        
        return new.next

       



















