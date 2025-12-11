"""You are given the head of a singly linked list and an integer x. Delete the xth node (1-based indexing) from the singly linked list.

Examples:

Input: x = 1,
    
Output: 2 -> 3 -> 1 -> 7
Explanation: After deleting the node at the 1st position (1-base indexing), the linked list is as
    
Input: x = 5,
    
Output: 2 -> 3 -> 4 -> 5
Explanation: After deleting the node at 5th position (1-based indexing), the linked list is as
    """

                                                            #CODE HERE:-


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def deleteNode(self, head, x):
        if x == 1:
            head = head.next
            return head
        l = 0
        curr = head
        while curr!=None:
            l+=1
            curr = curr.next
        
        curr = head
        if x==l:
            for i in range(1,x-1):
                curr = curr.next
            curr.next = None
            return head
        else:
            curr = head
            for i in range(1,x-1):
                curr = curr.next
            curr.next = curr.next.next
            return head