'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        current = head
        n=Node(x)
        if current == None:
            return n
        while current.next!=None:
            current=current.next
        current.next=n
        return head

  #https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1
