class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        def findKthElement(arr1, arr2, k):
            len1, len2 = len(arr1), len(arr2)
            
            if len1 > len2:
                return findKthElement(arr2, arr1, k)
            
            if len1 == 0:
                return arr2[k - 1]
            
            if k == 1:
                return min(arr1[0], arr2[0])
            

            i = min(len1, k // 2)
            j = min(len2, k // 2)
            
            if arr1[i - 1] > arr2[j - 1]:
                return findKthElement(arr1, arr2[j:], k - j)
            else:
                return findKthElement(arr1[i:], arr2, k - i)

        total_len = len(nums1) + len(nums2)
        
        if total_len % 2 == 1:
            return float(findKthElement(nums1, nums2, total_len // 2 + 1))
        else:
            left = findKthElement(nums1, nums2, total_len // 2)
            right = findKthElement(nums1, nums2, total_len // 2 + 1)
            return (left + right) / 2.0

