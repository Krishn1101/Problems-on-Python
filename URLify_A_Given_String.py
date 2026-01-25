"""Given a string s, replace all the spaces in the string with '%20'.

Examples:

Input: s = "Mr Benedict Cumberbatch"i love programming
Output: "Mr%20Benedict%20Cumberbatch"
Explanation: The 2 spaces are replaced by '%20'
Input: s = "i love programming"
Output: "i%20love%20programming"
Explanation: The 2 spaces are replaced by '%20'"""

                        #CODE HERE:-

class Solution:
    def URLify(self, s):
        s1 = ""
        for i in s:
            if i == " ":
                s1+="%20"
            else:
                s1+=i
        return s1