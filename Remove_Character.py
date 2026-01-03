"""Given two strings str1 and str2, remove those characters from the first string(str1) which are present in the second string(str2). Both the strings are different and contain only lowercase characters.
NOTE: Size of the first string is always greater than the size of the second string( |str1| > |str2|).
 

Example 1:

Input: str1 = "computer", str2= "cat"
Output: "ompuer"
Explanation: After removing characters(c, a, t) from string1 we get "ompuer".
Example 2:

Input: str1 = "occurrence", str2 = "car"
Output: "ouene"
Explanation: After removing characters (c, a, r) from string1 we get "ouene"."""

                                                        #CODE HERE:-

class Solution:
    def removeChars (ob, str1, str2):
        s = ""
        for i in str1:
            if i not in str2:
                s+=i
        return s