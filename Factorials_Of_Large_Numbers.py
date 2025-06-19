"""Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.

Examples:

Input: n = 5
Output: [1, 2, 0]
Explanation: 5! = 1*2*3*4*5 = 120
Input: n = 10
Output: [3, 6, 2, 8, 8, 0, 0]
Explanation: 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800
Input: n = 1
Output: [1]
Explanation: 1! = 1"""

                                                        #CODE HERE:-

class Solution:
    def factorial(self, n):
        p=1
        arr=[]
        for i in range(1,n+1):
            p=p*i
        for j in str(p):
            arr.append(int(j))
        return arr