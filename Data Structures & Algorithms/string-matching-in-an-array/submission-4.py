class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        for idx in range(len(words)):
            for count in range(len(words)):
                i = j = 0
                while i < len(words[count])  and j < len(words[idx]):
                    if words[count][i] == words[idx][j]:
                        i += 1
                        j += 1
                    else:
                        if i > 0:
                            i = 0
                            continue

                        j += 1

                if i == len(words[count]) and words[idx] != words[count]:
                    if words[count] in result:
                        continue
                    result.append(words[count])
        return result
            


        