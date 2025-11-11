"""The problem is to check whether the decimal representation of a given binary number is divisible by 5 or not.

Example 1:

Input: bin = "1010"
Output: "Yes"
Explanation: Decimal equivalent is
10 which is divisible by 5.
â€‹Example 2:

Input: bin = "1110"
Output: "No"
Explanation: Decimal equivalent is
14 which is not divisible by 5."""

                                                    #CODE HERE:-

class Solution:
    def isDivisibleBy5(self, Bin):
        ans = int(Bin,2)
        if ans%5==0:
            return 'Yes'
        else:
            return "No"