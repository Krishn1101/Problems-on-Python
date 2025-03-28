"""Given two sorted arrays a[] and b[] of size n and m respectively,
the task is to merge them in sorted order without using any extra space.
Modify a[] so that it contains the first n elements and modify b[] so
that it contains the last m elements."""

"""Examples:
1.
Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
Output:
2 2 3 4
7 10
Explanation: After merging the two non-decreasing arrays, we get, 2 2 3 4 7 10

2.
Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
Output:
1 2 3 5 8 9
10 13 15 20
Explanation: After merging two sorted arrays we get 1 2 3 5 8 9 10 13 15 20.

3.
Input: a[] = [0, 1], b[] = [2, 3]
Output:
0 1
2 3
Explanation: After merging two sorted arrays we get 0 1 2 3."""

                   # CODE HERE:-

class Solution:
    def mergeArrays(self, a, b):
        ft = len(a)-1
        sec = 0
        while(ft >= 0 and sec < len(b)):
            if(a[ft]>b[sec]):
                a[ft],b[sec] = b[sec],a[ft]
                ft-=1
                sec+=1
            else:
                break
        a.sort()
        b.sort()