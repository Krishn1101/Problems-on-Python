"""Given a string s containing only lowercase alphabets, the task is to sort it in lexicographically-descending order.

Examples:

Input: s = "geeks"
Output: "skgee"
Explanation: It's the lexicographically descending order.
Input: s = "for"
Output: "rof"
Explanation: "rof" is in lexicographically-descending order."""

                                                            #CODE HERE:-

class Solution:
    def ReverseSort(self, s):
        return "".join(sorted(s, reverse = True))