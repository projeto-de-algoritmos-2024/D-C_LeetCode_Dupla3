class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        def helper(nums, left, right):
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            left_max = helper(nums, left, mid)
            right_max = helper(nums, mid + 1, right)
            left_sum = float('-inf')  
            current_sum = 0

            for i in range(mid, left - 1, -1):  
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)  

            right_sum = float('-inf')  
            current_sum = 0
            for i in range(mid + 1, right + 1):  
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)  
            
            cross_sum = left_sum + right_sum

            return max(left_max, right_max, cross_sum)
        
        return helper(nums, 0, len(nums) - 1)
