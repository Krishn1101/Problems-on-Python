"""Given a number n. Return true if the digit sum(or sum of digits) of n is a Palindrome number otherwise false.

A Palindrome number is a number that stays the same when reversed

Examples:

Input: n = 56
Output: true
Explanation: The digit sum of 56 is 5+6 = 11. Since, 11 is a palindrome number.Thus, answer is true.
Input: n = 98
Output: false
Explanation: The digit sum of 98 is 9+8 = 17. Since 17 is not a palindrome,thus, answer is false."""

                                                #CODE HERE:-

class Solution:
    def isDigitSumPalindrome(self, n):
        l1 = list(map(int, str(n)))
        ans = sum(l1)
        ans1 = str(ans)
        ans1 = ans1[::-1]
        if(ans == int(ans1)):
            return True
        else:
            return False