# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        if head==None or head.next==None:
            return False
        a=[]
        while current!=None:
            if current.next in a:
                return True
            a.append(current.next)
            current=current.next
        return False