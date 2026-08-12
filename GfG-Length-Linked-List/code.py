''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        # code here
        current=head
        pos=1
        if head == None:
            return 0
        while current.next!=None:
            current=current.next
            pos+=1
        return pos

  #https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/1
