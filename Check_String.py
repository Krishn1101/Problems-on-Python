"""Given a string, check if all its characters are the same or not.

Example 1:

Input:
s = "geeks"
Output: False
Explanation: The string contains different
character 'g', 'e', 'k' and 's'.

Example 2:

Input: 
s = "gggg"
Output: True
Explanation: The string contains only one
character 'g'."""

                            #CODE HERE:-

class Solution:
    def check (self,s):
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        if len(freq.keys())==1:
            return True
        else:
            return False