"""Given a string consisting of lowercase letters, arrange all its letters in ascending order. 

Example 1:

Input:
S = "edcab"
Output: "abcde"
Explanation: characters are in ascending
order in "abcde".
Example 2:

Input:
S = "xzy"
Output: "xyz"
Explanation: characters are in ascending
order in "xyz"."""

                                            #CODE HERE:-

class Solution:
    def sort(self, s):
        ans = sorted(s)
        ans = "".join(ans)
        return ans