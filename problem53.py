class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Função auxiliar que vai fazer a mágica da divisão e conquista
        def helper(nums, left, right):
            # Se o intervalo tem apenas um elemento, retorna esse elemento
            if left == right:
                return nums[left]
            
            # Encontra o meio do intervalo
            mid = (left + right) // 2

            # Calcula a soma máxima do subarray na metade esquerda
            left_max = helper(nums, left, mid)

            # Calcula a soma máxima do subarray na metade direita
            right_max = helper(nums, mid + 1, right)
            
            # Agora precisamos calcular a soma máxima que cruza o meio

            # Inicializamos as variáveis para calcular a soma máxima à esquerda do meio
            left_sum = float('-inf')  # Começa com menos infinito para garantir que qualquer soma será maior
            current_sum = 0
            for i in range(mid, left - 1, -1):  # Vamos do meio até o início do intervalo
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)  # Mantém a maior soma encontrada

            # Inicializamos as variáveis para calcular a soma máxima à direita do meio
            right_sum = float('-inf')  # Também começa com menos infinito
            current_sum = 0
            for i in range(mid + 1, right + 1):  # Vamos do meio + 1 até o fim do intervalo
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)  # Mantém a maior soma encontrada
            
            # A soma máxima que cruza o meio é a soma das maiores somas à esquerda e à direita
            cross_sum = left_sum + right_sum
            
            # Retorna o maior valor entre as três opções:
            # 1. A maior soma na metade esquerda
            # 2. A maior soma na metade direita
            # 3. A maior soma que cruza o meio
            return max(left_max, right_max, cross_sum)
        
        # Chamamos a função auxiliar com os índices do início e do fim do array
        return helper(nums, 0, len(nums) - 1)
