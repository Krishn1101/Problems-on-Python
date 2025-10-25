"""Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: We get the sorted array after using merge sort
Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Explanation: We get the sorted array after using merge sort """

                                                        #CODE HERE:-

def merge(self,arr,l,mid,r):
    a = []
    b = []
    for i in range(l,mid+1):
        a.append(arr[i])
    for i in range(mid+1,r+1):
        b.append(arr[i])
        
    i,j,k = 0,0,l
    
    while k<=r:
        if j==len(b):
            arr[k] = a[i]
            i+=1
            k+=1
        elif i == len(a):
            arr[k] = b[j]
            j+=1
            k+=1
        elif a[i]<b[j]:
            arr[k] = a[i]
            i+=1
            k+=1
        else:
            arr[k] = b[j]
            j+=1
            k+=1
    
def mergeSort(self, arr, l, r):
    #base case:-
    if l>=r:
        return
    
    #recursive case:-
    mid = (l+r)//2
    
    self.mergeSort(arr,l,mid)
    self.mergeSort(arr,mid+1,r)
    
    self.merge(arr,l,mid,r)
    
def sortArray(self,arr):
    mergeSort(arr,0,len(arr)-1)
    return arr
        