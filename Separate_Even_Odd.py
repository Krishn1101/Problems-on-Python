"""You are given a list numbers that contains integers. You need to return two lists, one of even numbers and other of odd numbers.

Examples:

Input: arr = [54, 43, 2, 5, 14, 17, 18, 9]
Output: even: 54 2 14 18, odd: 43 5 17 19
Input: arr = [5, 6, 7, 2, 4, 8, 9]
Output: even: 6 2 4 8, odd: 5 7 9"""

                                                            #CODE HERE:-

def evenOdd(arr):
    even = []
    odd = []
    for i in arr:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return (even, odd)
