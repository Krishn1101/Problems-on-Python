"""Geek is very fond of patterns. Once, his teacher gave him a square pattern to solve. He gave Geek an integer n and asked him to build a pattern.

Help Geek to build a square pattern with the help of *  such that each * is space-separated in each line.

Example 1:

Input:
n = 3
Output:
* * *
* * *
* * *
Example 2:

Input:
n = 5
Output:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *"""

                                                            #CODE HERE:-

class Solution:
    def printSquare(self, N):
        for i in range(N):
            for j in range(N):
                print("*", end = " ")
            print("")