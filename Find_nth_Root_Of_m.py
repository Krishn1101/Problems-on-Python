"""You are given 2 numbers n and m, the task is to find n√m (nth root of m). If the root is not integer then returns -1.

Examples :

Input: n = 3, m = 27
Output: 3
Explanation: 33 = 27
Input: n = 3, m = 9
Output: -1
Explanation: 3rd root of 9 is not integer.
Input: n = 4, m = 625
Output: 5
Explanation: 54 = 625"""

                                                        #CODE HERE:-

class Solution:
    def nthRoot(self, n, m):
        a = round(m**(1/n))
        if(a**n==m):
            return a
        else:
            return -1