"""You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube.

Examples:

Input: n = 6
Output: 1
Explanation: For dice facing number 6 opposite face will have the number 1.
Input: n = 2
Output: 5
Explanation: For dice facing number 5 opposite face will have the number 2."""

                                                            #CODE HERE:-

class Solution:
    def oppositeFaceOfDice(self, n):
        if(n==6):
            return 1
        elif(n==2):
            return 5
        elif(n==3):
            return 4
        elif(n==4):
            return 3
        elif(n==5):
            return 2
        elif(n==1):
            return 6