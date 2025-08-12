"""Given a number N. check whether a given number N  is palindrome or not in it's both formates (Decimal and Binary ).

Example 1:

Input: N = 7
Output: "Yes" 
Explanation: 7 is palindrome in it's decimal 
and also in it's binary (111).So answer is "Yes".
Example 2:

Input: N = 12
Output: "No"
Explanation: 12 is not palindrome in it's decimal
and also in it's binary (1100).So answer is "No". """

                                                #CODE HERE:-

#User function Template for python3
class Solution:
    def isDeciBinPalin (self, N):
        int_a = str(N)
        int_a = int_a[::-1]
        if(int(int_a) == N):
            bin_a = bin(N)
            bin_b = str(bin_a)
            bin_b = bin_b[::-1]
            if(bin_b[:-2] == bin_a[2:]):
                return "Yes"
        return "No"