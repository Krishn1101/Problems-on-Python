"""You are given a singly linked list of n elements, and also an element x. You need to find if x is present in the linked list or not. Return true if x is present else returns false. (1 is printed by the driver code if the returned value is true, otherwise 0)

Examples :

Input: LinkedList: 1->2->3->4->5, x = 4
Output: 1
Input: LinkedList: 2->4->6->7->5->1->0, x = 10
Output: 0"""

                                                                #CODE HERE:-

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def searchLinkedList(self, head, x):
        curr = head
        
        while curr!=None:
            if curr.data == x:
                return True
            else:
                curr = curr.next
        return False