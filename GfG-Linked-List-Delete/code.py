''' Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        #code here
        current = head
        pos=1
        if x==1:
            head=current.next
            return head
        while pos<x-1:
            current=current.next
            pos+=1
        current.next=current.next.next
        return head
        
