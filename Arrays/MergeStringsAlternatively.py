class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, f = 0, 0
        n = []
        while i < len(word1) and f < len(word2):
            n.append(word1[i])
            n.append(word2[f])
            i += 1
            f += 1
        n.append(word1[i:])
        n.append(word2[f:])

        return "".join(n)



