"""Given three distinct numbers a, b and c. Find the number with a value in the middle (Try to do it with minimum comparisons).

Examples :

Input: a = 978, b = 518, c = 300
Output: 518
Explanation: Since 518>300 and 518<978, so 518 is the middle element.
Input: a = 162, b = 934, c = 200
Output: 200
Exaplanation: Since 200>162 && 200<934, So, 200 is the middle element.
Input: a = 246, b = 214, c = 450
Output: 246"""

                                                        #CODE HERE:-

class Solution:
    def middle(self, a, b, c):
        arr=[]
        arr.append(a)
        arr.append(b)
        arr.append(c)
        arr.sort()
        return(arr[1])