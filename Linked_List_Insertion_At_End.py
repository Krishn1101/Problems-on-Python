"""You are given the head of a Singly Linked List and a value x, insert that value x at the end of the LinkedList and return the head of the modified Linked List.

Examples :

Input: x = 6,
   
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Explanation: We can see that 6 is inserted at the end of the linkedlist.
   
Input: x = 1,
   
Output: 4 -> 5 -> 1
Explanation: We can see that 1 is inserted at the end of the linked list."""

                                                            #CODE HERE:-

    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insertAtEnd(self, head, x):
        if head == None:
            return Node(x)
        curr = head
        while curr.next!=None:
            curr = curr.next
            
        curr.next = Node(x)
        
        return head