"""Given a string s consisting of only '0's and '1's,  find the last index of the '1' present.

Note: If '1' is not present, return "-1"

Examples:

Input: s = 00001
Output: 4
Explanation: Last index of  1 in given string is 4.
Input: s = 0
Output: -1
Explanation: Since, 1 is not present, so output is -1."""

                                            #CODE HERE:-
                                            
class Solution:
    def lastIndex(self, s: str) -> int:
        freq = {}
        for i in range(len(s)):
            if s[i] == "1":
                freq[i] = i
        if "1" not in s:
            return -1
        else:
            return max(freq.values())