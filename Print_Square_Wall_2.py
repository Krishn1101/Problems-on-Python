"""Given an integer s,  write a program to print a square wall of size s without using string multiplication. Use nested loops instead. The * character will make up the wall.

Before submitting code, verify it by running offline. Does your square visually looks like a square?

Example 1:

Input:
s = 5
Output:

Explanation:
Its perfect square wall. """

                                                        #CODE HERE:-

def squareWall(s):
    for i in range(s):
        for j in range(s):
            print("*", end = " ")
        print()