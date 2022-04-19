"""
Longest Palindromic Substring
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # Form a bottom-up dp 2d array
        # dp[i][j] will be 'true' if the string from index i to j is a palindrome.
        dp = [[False] * n for _ in range(n)]
        res = ""

        # every string with one character is a palindrome
        for i in range(n):
            dp[i][i] = True

        for end in range(1, n):
            for start in range(end):
                if s[start] == s[end]:
                    # if it's a two char. string or if the remaining string is a palindrome too
                    if end - start == 1 or dp[start + 1][end - 1] is True:
                        dp[start][end] = True
                        if len(res) < end - start + 1:
                            res = s[start:end + 1]
        return res