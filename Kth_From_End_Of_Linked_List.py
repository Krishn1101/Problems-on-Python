"""You are given the head of a linked list and the number k, You have to return the kth node from the end of linkedList. If k is more than the number of nodes, then the return -1.

Examples

Input: LinkedList: 1->2->3->4->5->6->7->8->9, k = 2
Output: 8
Explanation: The given linked list is 1->2->3->4->5->6->7->8->9. The 2nd node from end is 8.

Input: LinkedList: 10->5->100->5, k = 5
Output: -1
Explanation: The given linked list is 10->5->100->5. Since 'k' is more than the number of nodes, the output is -1.
"""

                                                        #CODE HERE:-

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
	

class Solution:
    def getKthFromLast(self, head, k):
        l = 0
        
        curr = head
        
        while curr!=None:
            l+=1
            curr = curr.next
        
        ans = l-k
        
        if k>l:
            return -1
        curr = head
        for i in range(ans):
            curr = curr.next
            
        return curr.data