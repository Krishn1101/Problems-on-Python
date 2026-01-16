"""You are given a string s consisting of multiple words. You need to count the total words in the string. Words are separated by a single space.
Note: It is guaranteed that the last character of the given string is not a white space.

Examples:

Input: s = "Geeks"
Output: 1
Explanation: There is just one word in the given sentence
Input: s = "World is hello"
Output: 3
Explanation: There exists three words in the given sentence"""

                                                    #CODE HERE:-

class Solution:
    def countWords(self,s):
        return(len(s.split()))