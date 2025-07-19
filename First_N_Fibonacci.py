"""Given a number n, return an array containing the first n Fibonacci numbers.

Note: The first two numbers of the series are 0 and 1.

Examples:

Input: n = 5
Output: [0, 1, 1, 2, 3]
Input: n = 7
Output: [0, 1, 1, 2, 3, 5, 8]
Input: n = 2
Output: [0, 1]"""

                            #CODE HERE:-

class Solution:
    def fibonacciNumbers(self,n):
        a = 0
        b = 1
        c = 0 
        arr = [0]
        if(n==1):
            return arr
        elif(n==2):
            arr.append(b)
        else:
            arr.append(b)
            for i in range(2,n):
                c=a+b
                arr.append(c)
                a=b
                b=c
        return arr