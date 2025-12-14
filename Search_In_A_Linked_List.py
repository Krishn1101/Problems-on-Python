"""Given a linked list with the head node and a key, the task is to check if the key is present in the linked list or not. Return true if key is present, else return false.

Example:

Input: key = 3,
      
Output: true
Explanation: 3 is present in Linked List.

Input: key = 4,
   
Output: false
Explanation: 4 is not present in Linked List."""

                                                            #CODE HERE:-


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def searchKey(self, head, key):
        curr = head
        
        while curr!=None:
            if curr.data == key:
                return True
            else:
                curr = curr.next
        return False