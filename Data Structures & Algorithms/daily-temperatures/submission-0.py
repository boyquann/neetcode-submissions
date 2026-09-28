class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(waiting) > 0 and temperatures[i] > temperatures[waiting[-1]]:
                index = waiting.pop()
                answer[index] = i - index

            waiting.append(i)

        return answer




