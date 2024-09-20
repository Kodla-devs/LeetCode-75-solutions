class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split()

        reversed_words = words[::-1]

        return " ".join(reversed_words)
        