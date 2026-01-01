"""Given a string s. Your task is to remove spaces from it. 

Examples:

Input: s = "geeks  for geeks"
Output: "geeksforgeeks"
Explanation: All the spaces have been removed.
Input: s = "    g f g"
Output: "gfg"
Explanation: All the spaces including the leading ones have been removed."""

                            #CODE HERE:-

class Solution:
    def modify(self, s):
        ans = ""
        
        for i in s:
            if i!=" ":
                ans+=i
        return ans