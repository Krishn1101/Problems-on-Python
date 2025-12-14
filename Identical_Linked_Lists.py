"""Given the heads of two singly linked lists, head1 and head2, the task is to determine whether the two linked lists are identical. Two linked lists are considered identical if they have the same number of nodes and each corresponding node contains the same data in the same order. Return true if both lists are identical; otherwise, return false.

Examples:

Input: head1: 1->2->3->4->5->6, head2: 99->59->42->20
Output: false
Explanation:

As shown in figure the two lists are not identical.
Input: head1: 1->2->3->4->5, head2: 1->2->3->4->5
Output: true
Explanation: 
 
As shown in figure both are identical."""

                                                            #CODE HERE:-


# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def areIdentical(self, head1, head2):
        l1 = 0
        l2 = 0
        
        curr1 = head1
        curr2 = head2
        
        while curr1!=None:
            l1+=1
            curr1 = curr1.next
        while curr2!=None:
            l2+=1
            curr2 = curr2.next
        if l1!=l2:
            return False
        else:
            while head1 and head2:
                if head1.data != head2.data:
                    return False
                head1 = head1.next
                head2 = head2.next
            return True