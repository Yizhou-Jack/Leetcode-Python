class Solution:
    def longestNiceSubstring(self, s):
        if len(s) < 2:
            return ""

        def helper(s):
            chars = set(list(s))
            for i in range(len(s)):
                if not (s[i].lower() in chars and s[i].upper() in chars):
                    s1 = helper(s[:i])
                    s2 = helper(s[i+1:])
                    return s2 if len(s2) > len(s1) else s1
            return s

        res = helper(s)
        return res