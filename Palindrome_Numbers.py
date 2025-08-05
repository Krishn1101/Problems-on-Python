"""Check if the binary representation of a number is palindrome or not.
 

Example 1:

Input:
N = 17
Output:
1
Explanation:
(17)10 = (10001)2
Which is pallindrome hence
output is 1.

Example 2:

Input:
N = 16
Output:
0
Explanation:
(16)10 = (10000)2
Which is not pallindrome 
hence output is 0."""

                            #CODE HERE:-

#User function Template for python3

class Solution:
    def isPallindrome(self, N):
        ans = bin(N)[2:]                    #ye [2:] issliye kiye kyu ki humara answer 0b1001 aise aata hai toh shuru ke 0b hatane ke liye me aise kiya hu...
        ans1 = str(ans)
        ans1 = ans1[::-1]
        if(ans == ans1):
            return 1
        else:
            return 0