"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5."""

                                                #CODE HERE:-

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        import math
        nums1.extend(nums2)
        nums1.sort()
        o = len(nums1)
        if o%2!=0:
            ans = math.ceil(o/2)
            return(nums1[ans-1])
        else:
            ans = int(o/2)
            return((nums1[ans-1] + nums1[ans])/2)