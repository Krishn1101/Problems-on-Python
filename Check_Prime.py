"""Given an integer n check if n is prime or not.

A prime number is a number that is divisible by 1 and itself only.

Examples:

Input: n = 17
Output: True 
Explanation: 17 is  divisible by only 1 and 17. So it's a prime number.
Input: n = 56
Output: False
Explanation: 56 is divisible by 2, 4, 7.....etc. So its not a prime number."""

                                    #CODE HERE:-

def prime(n):
    ans = n//2
    if n == 1:
        return False
    else:
        for i in range(2,ans+1):
            if n%i==0:
                return False
        return True