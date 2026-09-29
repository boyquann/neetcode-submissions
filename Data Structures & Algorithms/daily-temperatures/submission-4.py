class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for idx, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                popped = stack.pop()
                result[popped[1]] = idx - popped[1]

            stack.append((val, idx))

        return result




            


