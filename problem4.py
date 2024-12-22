class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
     
        # Garantir que nums1 seja o menor array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # Elementos adjacentes aos cortes
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Verificar condições da mediana
            if maxX <= minY and maxY <= minX:
                # Caso total de elementos ímpar
                if (x + y) % 2 == 1:
                    return max(maxX, maxY)
                # Caso total de elementos par
                return (max(maxX, maxY) + min(minX, minY)) / 2.0
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1
        