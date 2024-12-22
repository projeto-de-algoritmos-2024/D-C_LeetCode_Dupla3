class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Função auxiliar para encontrar o k-ésimo menor elemento em dois arrays ordenados
        def findKthElement(arr1, arr2, k):
            len1, len2 = len(arr1), len(arr2)
            
            # Garante que arr1 seja o menor dos dois arrays
            if len1 > len2:
                return findKthElement(arr2, arr1, k)
            
            # Se arr1 está vazio, o k-ésimo menor é simplesmente o k-ésimo elemento de arr2
            if len1 == 0:
                return arr2[k - 1]
            
            # Se estamos procurando o primeiro elemento, retornamos o menor entre os primeiros elementos de arr1 e arr2
            if k == 1:
                return min(arr1[0], arr2[0])
            
            # Dividimos k em duas partes: i e j
            # i não pode ser maior que o tamanho de arr1 e j não pode ser maior que o tamanho de arr2
            i = min(len1, k // 2)
            j = min(len2, k // 2)
            
            # Compara os elementos arr1[i-1] e arr2[j-1]
            if arr1[i - 1] > arr2[j - 1]:
                # Se arr1[i-1] é maior, descartamos os primeiros j elementos de arr2
                # e ajustamos k para k - j
                return findKthElement(arr1, arr2[j:], k - j)
            else:
                # Caso contrário, descartamos os primeiros i elementos de arr1
                # e ajustamos k para k - i
                return findKthElement(arr1[i:], arr2, k - i)

        # Calcula o comprimento total dos dois arrays
        total_len = len(nums1) + len(nums2)
        
        # Se o comprimento total é ímpar, a mediana é o elemento do meio
        if total_len % 2 == 1:
            return float(findKthElement(nums1, nums2, total_len // 2 + 1))
        else:
            # Se o comprimento total é par, a mediana é a média dos dois elementos do meio
            left = findKthElement(nums1, nums2, total_len // 2)
            right = findKthElement(nums1, nums2, total_len // 2 + 1)
            return (left + right) / 2.0

