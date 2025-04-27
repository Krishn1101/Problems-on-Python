"""Given two integer arrays nums1 and nums2,
return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted."""

                                                            #CODE HERE:-

#METHOD(i):-
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a=set()
        b=set()
        for i in range(len(nums1)):
            a.add(nums1[i])
        for j in range(len(nums2)):
            b.add(nums2[j])
        return (list(a.intersection(b)))
    

#METHOD(ii):-
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a=[]
        sz1=len(nums1)
        sz2=len(nums2)
        if(sz1>sz2):
            for i in range(len(nums2)):
                if(nums2[i] in nums1 and nums2[i] not in a):
                    a.append(nums2[i])
                else:
                    i+=1
        elif(sz1<=sz2):
            for j in range(len(nums1)):
                if(nums1[j] in nums2 and nums1[j] not in a):
                    a.append(nums1[j])
                else:
                    j+=1
        return a