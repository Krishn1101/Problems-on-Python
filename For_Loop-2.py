"""You are given a string s, you need to print its characters at even indices (index starts at 0).

Examples:

Input: s = "Geeks"
Output: Ges
Explanation: The even indices characters are printed.
Input: s = "DoctorPhenomenal"
Output: DcoPeoea
Explanation: The even indices characters are printed."""

                                                #CODE HERE:-

class Solution:
    def print_even_indices(self, s: str):
        for i in range(len(s)):
            if i%2==0:
                print(s[i],end = "")