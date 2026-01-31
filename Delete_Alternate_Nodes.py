"""Given a Singly Linked List, Delete all alternate nodes of the list ie delete all the nodes present in even positions.

Examples :

Input: LinkedList: 1->2->3->4->5->6
 
Output: 1->3->5

Explanation: Deleting alternate nodes ie 2, 4, 6 results in the linked list with elements 1->3->5.
Input: LinkedList: 99->59->42->20
 
Output: 99->42"""

                                                    #CODE HERE:-

'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None'''

class Solution:
    def deleteAlt(self, head):
        curr = head
        if not curr.next:
            return head
        else:
            while(curr.next!=None):
                if curr.next.next:
                    curr.next = curr.next.next
                    curr = curr.next
                else:
                    curr.next = None
        return head