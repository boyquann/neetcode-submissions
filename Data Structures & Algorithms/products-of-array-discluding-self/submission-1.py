class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        left_pass = [1] * len(nums)
        right_pass = [1] * len(nums)

        for i in range(1, len(nums)):
            left_pass[i] = left_pass[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right_pass[i] = right_pass[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            output[i] = left_pass[i] * right_pass[i]

        return output

