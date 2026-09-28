class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        areas = []

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)

            areas.append(area)

            if heights[left] > heights[right]:
                right -= 1

            elif heights[left] < heights[right]:
                left += 1

            else:
                left += 1

        max = areas[0]

        for i in range(1, len(areas)):
            if max < areas[i]:
                max = areas[i]

        return max



        