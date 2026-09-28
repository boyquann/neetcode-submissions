class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 1
        right = len(nums) - 1
        result = []
        nums_sort = sorted(nums)

        for i in range(len(nums_sort)):
            left = i + 1
            right = len(nums_sort) - 1

            if i > 0 and nums_sort[i] == nums_sort[i - 1]:
                continue

            while left < right:
                if nums_sort[i] + nums_sort[left] + nums_sort[right] > 0:
                    right -= 1

                elif nums_sort[i] + nums_sort[left] + nums_sort[right] < 0:
                    left += 1

                else:
                    result.append([nums_sort[i], nums_sort[left], nums_sort[right]])
                    left += 1
                    right -= 1

                    while (nums_sort[left] == nums_sort[left - 1] and left < right):
                        left += 1

                    while (nums_sort[right] == nums_sort[right + 1] and left < right):
                        right -= 1

                if left >= right:
                    break

        return result    


                

        