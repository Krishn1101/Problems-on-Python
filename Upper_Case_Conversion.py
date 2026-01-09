"""Given a string s, convert the first letter of each word in the string to uppercase. 

Examples:

Input: s = "gEEKs"
Output: "GEEKs"
Input: s = "i love programming"
Output: "I Love Programming"""

                                        #CODE HERE:-

class Solution:
    def convert(self, s):
        ans = s.split(" ")
        p = ""
        for i in ans:
            i = i.capitalize()
            p = p + i
            p+=" "
        return p.strip()