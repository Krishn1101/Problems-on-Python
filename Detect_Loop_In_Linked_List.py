"""You are given the head of a singly linked list. You have to determine whether the given linked list contains a loop or not. A loop exists in a linked list if the next pointer of the last node points to any other node in the list (including itself), rather than being null.

Note: Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to. If pos = 0, it means the last node points to null. Note that pos is not passed as a parameter.

Examples:

Input: pos = 2,
   
Output: true
Explanation: There exists a loop as last node is connected back to the second node.
Input: pos = 0,
   
Output: false
Explanation: There exists no loop in given linked list.
Input: pos = 1,
   
Output: true
Explanation: There exists a loop as last node is connected back to the first node."""

                                                            #CODE HERE:-


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def detectLoop(self, head):
        curr = head
        arr = set()
        
        while curr:
            if curr not in arr:
                arr.add(curr)
                curr = curr.next
            else:
                return True
        return False