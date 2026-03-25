"""You are given an integer array arr[]. You need to push the elements of the array into a stack and then print them while popping.
Note: No need to print extra line after printing the stack elements.

Examples:

Input: arr = [1, 2, 3, 4, 5]
Output: 5 4 3 2 1
Explanation: Elements are pushed and then popped from the top of the stack in the order 5, 4, 3, 2, 1.
Input: arr = [1, 6, 43, 1, 2, 0, 5]
Output: 5 0 2 1 43 6 1"""

                                                #CODE HERE:-

class Solution:
    def __init__(self):
        self.st = []
    def _push(self, arr):
        self.st.extend(arr)
    def _pop(self, stack):
        if len(self.st) == 0:
            return -1
        else:
            for i in range(len(self.st)):
                x = self.st[-1]
                self.st.pop()
                print(x,end = " ")