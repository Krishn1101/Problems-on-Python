"""Given an n-digit large number n in form of string, check whether it is divisible by 7 or not. Return 1 if divisible by 7, otherwise 0.

Examples :

Input: n = "49"
Output: 1
Explanation: 49 is divisible by 7.
Input: n = "1000"
Output: 0
Explanation: 1000 is not divisible by 7."""

                                                                    #CODE HERE:-

class Solution:
    def isdivisible7(self, num):
        import sys
        sys.set_int_max_str_digits(100000)
        num = int(num)
        if num%7==0:
            return 1
        else:
            return 0