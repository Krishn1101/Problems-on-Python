"""You are given a string s. Remove all characters except the numeric characters from an alphanumeric string.

Examples:

Input: s = "AA1d23cBB4"
Output: "1234"
Explanation: Remove all characters other than numbers
Input: s= "a1b2c3"
Output: "123"
Explanation: Remove all characters other than numbers"""

                                                #CODE HERE:-

class Solution:
    def removeCharacters(self, s):
        ans = ""
        for i in s:
            if 48<=ord(i)<=57:
                ans+=i
        return ans