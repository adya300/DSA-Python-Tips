'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        #Code here
        current=head
        if head.data==key:
            return True
        while current.next!=None:
            current=current.next
            if current.data==key:
                return True
        return False


#https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1
