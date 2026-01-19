"""Given a string s consisting of upper/lower-case alphabets and empty space characters ‘ ‘. The string may contain spaces at the end. You will have return the length of last word which consists of alphabets only.

Examples :

Input: s = "Geeks for Geeks"
Output: 5
Explanation: The last word is "Geeks" of length 5.
Input: s = "Start Coding Here "
Output: 4
Explanation: The last word is "Here" of length 4."""

                                                        #CODE HERE:-

class Solution:
    def findLength(self, s):
        ans = s.split()
        return(len(ans[-1]))