"""You are given the heads of two non-empty singly linked lists, head1 and head2, that intersect at a certain point. Return that Node where these two linked lists intersect.

Note: It is guaranteed that the intersected node always exists.

In the custom input you have to give input for CommonList which pointed at the end of both head1 and head2 to form a Y-shaped linked list.
Examples:

Input: head1: 10 -> 15 -> 30, head2: 3 -> 6 -> 9 -> 15 -> 30
Output: 15
Explanation: From the above image, it is clearly seen that the common part is 15 -> 30, whose starting point is 15.
    
Input: head1: 4 -> 1 -> 8 -> 5, head2: 5 -> 6 -> 1 -> 8 -> 5
Output: 1
Explanation: From the above image, it is clearly seen that the common part is 1 -> 8 -> 5, whose starting point is 1.
    """

                                                            #CODE HERE:-


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def intersectPoint(self, head1, head2):
        l1 = 0
        l2 = 0
        curr = head1
        while curr!=None:
            l1+=1
            curr = curr.next
        
        curr = head2
        while curr!=None:
            l2+=1
            curr = curr.next
        
        if l1>l2:
            l = l1-l2
            for i in range(l):
                head1 = head1.next
            
        elif l1<l2:
            l = l2-l1
            for i in range(l):
                head2 = head2.next
        
        b = True
        while(b):
            if head1 == head2:
                b = False
                return head1
            else:
                head1 = head1.next
                head2 = head2.next