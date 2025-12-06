"""Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]"""

                                #CODE HERE:-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        last = head
        l = 0
        while last.next!=None:
            last = last.next
            l+=1
        l+=1

        k = k%l
        if k == 0:
            return head
        else:
            curr = head
            for i in range(l-k-1):
                curr = curr.next
            last.next = head
            head = curr.next
            curr.next = None
        return head