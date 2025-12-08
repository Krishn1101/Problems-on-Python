"""You are given the head of a singly linked list. Return an array containing the values of the nodes.

Examples:

Input:
    
Output: [1, 2, 3, 4, 5]
Explanation: The linked list contains 5 elements [1, 2, 3, 4, 5]. The elements are printed in a single line.
Input:
    
Output: [10, 20, 30, 40, 50, 60]
Explanation: The linked list contains 5 elements [10, 20, 30, 40, 50, 60]. The elements are printed in a single line."""

                                                #CODE HERE:-


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def printList(self, head):
        arr = []
        curr = head
        while curr!=None:
            arr.append(curr.data)
            curr = curr.next
            if curr == None:
                break
        return arr