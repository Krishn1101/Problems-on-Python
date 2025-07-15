"""Given a number represented as a string s (which may be very large), check whether it is divisible by 13 or not.

Examples:

Input : s = "2911285"
Output : true
Explanation: 2911285 / 13 = 223945, which is a whole number with no remainder.
Input : s = "27"
Output : false
Explanation: 27 / 13 ≈ 2.0769..., which is not a whole number (there is a remainder)."""

                                                        #CODE HERE:-

class Solution:
    def divby13(self, s):
        remainder = 0
        for digit in s:
            remainder = (remainder * 10 + int(digit)) % 13
        return remainder == 0