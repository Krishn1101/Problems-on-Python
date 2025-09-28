"""Given an integer n, write a program to return the factorial of n. The Factorial of a number is the product of all the numbers from 1 to n.

Note: 0 factorial is equal to 1.

Example:

Input: n = 5
Output: 120
Explanation: 1 * 2 * 3 * 4 * 5 = 120
Input: n = 10
Output: 3628800
Explanation: 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 = 3628800"""

                                                        #CODE HERE:-

def fact(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans*i
    return ans

n = int(input())
print(fact(n))