"""You are given two integer numbers in the form of string, the base a and the index b. You have to find the last digit of ab.

Examples:

Input: a = "3", b = "10"
Output: 9
Explanation: 310 = 59049. Last digit is 9.
Input: a = "6", b = "2"
Output: 6
Explanation: 62 = 36. Last digit is 6."""

                                                        #CODE HERE:-
                                                        
class Solution:
    def getLastDigit(self, a, b):
        return(pow(int(a),int(b),10))