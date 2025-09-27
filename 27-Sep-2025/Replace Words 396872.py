# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = set(dictionary)
        words = sentence.split()

        def helper(word):
            for i in range(1, len(word)+1):
                prefix = word[:i]
                if prefix in root:
                    return prefix
            return word

        res = " ".join(helper(word) for word in words)
        return res

        