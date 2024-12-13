class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prev = list(range(len(word2)+1))
        cur = [0] * (len(word2) + 1)

        for i in range(1, len(word1) + 1):
            cur[0] = i
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    cur[j] = prev[j-1]
                else:
                    cur[j] = min(prev[j-1] + 1, prev[j] + 1 , cur[j-1] + 1)
            prev = cur
            cur = [0] * (len(word2) + 1)
        
        return prev[-1]