"""Given the head, the head of a singly linked list, Returns true if the linked list is circular & false if it is not circular.

A linked list is called circular if it is not NULL terminated and all nodes are connected in the form of a cycle. 

Note: The linked list does not contain any inner loop.

Examples:

Input: 

Output: true
Explanation: As shown in figure the first and last node is connected, i.e. 5 --> 2
Input: 
 
Output: false
Explanation: As shown in figure this is not a circular linked list."""

                                                        #CODE HERE:-

class Node:
   def __init__(self, data):
       self.data = data
       self.next = None


# your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def isCircular(self, head):
        arr = set()
        
        curr = head
        
        while curr!=None:
            if curr not in arr:
                arr.add(curr)
                curr = curr.next
            else:
                return True
        return False