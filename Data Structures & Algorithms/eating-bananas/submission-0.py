class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            total_hours = 0
            mid = (left + right) // 2

            for p in piles:
                total_hours += math.ceil(p / mid)

            if total_hours <= h:
                result = mid
                right = mid - 1

            else:
                left = mid + 1

        return result
