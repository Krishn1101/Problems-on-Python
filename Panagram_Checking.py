"""Given a string s, check if it is a "Panagram" or not. Return true if the string is a Panagram, else return false.
A "Panagram" is a sentence containing every letter in the English Alphabet either in lowercase or Uppercase.

Examples:

Input: s = "Bawds jog, flick quartz, vex nymph"
Output: true
Explanation: In the given string, there are all the letters of the English alphabet. Hence, the output is true.
Input: s = "sdfs"
Output: false
Explanation: In the given string, there aren't all the letters present in the English alphabet. Hence, the output is false."""

                                                        #CODE HERE:-

class Solution:
    def checkPangram(self,s):
        s = s.lower()
        ans =  ""
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(s)):
            if 97<=ord(s[i])<=122 and s[i]!= " ":
                if s[i] not in ans:
                    ans+=s[i]
        for i in alpha:
            if i not in ans:
                return False
        return True