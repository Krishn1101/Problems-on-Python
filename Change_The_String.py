"""Given a string s, the task is to change the complete string to uppercase or lowercase depending on the case of the first character.

Examples:

Input: s = "abCD"
Output: "abcd"
Explanation: The first letter (a) is lowercase. Hence, the complete string is made lowercase.
Input: s = "Abcd"
Output: "ABCD"
Explanation: The first letter (A) is uppercase. Hence, the complete string is made uppercase."""

                                                        #CODE HERE:-

class Solution:
    def modify(self, s):
        a = s[0]
        if 97<=ord(a)<=122:
            return s.lower()
        elif 65<=ord(a)<=90:
            return s.upper()