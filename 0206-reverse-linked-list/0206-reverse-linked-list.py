# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        poi=None
        if head==None or head.next==None:
            return head
        while current.next!=None:
            a=current
            next_node=current.next
            a.next=poi
            poi=a
            current=next_node
        next_node.next=poi
        return next_node