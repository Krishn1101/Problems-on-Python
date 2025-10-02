"""Given a non-empty sequence of characters s, return true if sequence is Binary, else return false.

Examples:

Input: s = "101"
Output: true
Explanation: Since string contains only '0' and '1', output is true.
Input: s = "75"
Output: false
Explanation: Since string contains digits other than '0' and '1', output is false."""

                                            #CODE HERE:-

class Solution:
    def isBinary(self, s):
        for i in s:
            if i not in "01":
                return False
        return True