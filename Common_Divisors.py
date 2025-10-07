"""Given two integer numbers a and b, the task is to find count of all common divisors of given numbers.

Example 1:

Input: a = 12, b = 24
Output: 6 
Explanation: all common divisors 
are 1, 2, 3, 4, 6 and 12.

Example 2:

Input: a = 3, b = 17
Output: 1
Explanation: all common divisors are 1."""

                                                    #CODE HERE:-

class Solution:
    def commDiv (self, a, b):
        cnt = 0
        if a<b:
            for i in range(1,a+1):
                if a%i==0 and b%i==0:
                    cnt+=1
        else:
            for i in range(1,b+1):
                if a%i==0 and b%i==0:
                    cnt+=1
        return cnt