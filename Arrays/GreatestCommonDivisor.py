class Solution(object):
    def gcdOfStrings(self, str1, str2):
        len1, len2 = len(str1), len(str2)

        def isDivisor(i):
            if len1 % i or len2 % i:
                return False
            f1, f2 = len1 // i, len2 // i
            return str1[:i] * f1 == str1 and str2[:i] * f2

        for i in range(min(len1, len2), 0, -1):
            if isDivisor(str1[:i]):
                return str1[:i]


