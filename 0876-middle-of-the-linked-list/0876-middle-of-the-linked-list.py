# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        a=head
        pos=1
        while current.next != None:
            current = current.next
            pos+=1
        x=pos/2
        z=1
        if x<1:
            return head
        if type(x)==float:
            x=int(x)+1
        while z<x :
            a=a.next
            z+=1
        head=a
        return head
