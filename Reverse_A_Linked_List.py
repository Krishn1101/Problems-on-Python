"""You are given the head of a singly linked list. You have to reverse the linked list and return the head of the reversed list.

Examples:

Input:
      
Output: 4 -> 3 -> 2 -> 1
Explanation: After reversing the linkedList
      
Input: 
      
Output: 8 -> 9 -> 10 -> 7 -> 2
Explanation: After reversing the linked list
      
Input: 
      
Output: 8
Explanation:
       """

                                                            #CODE HERE:-


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    def reverseList(self, head):
        curr = head
        prev = None
        nxt = None
        while curr!=None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev