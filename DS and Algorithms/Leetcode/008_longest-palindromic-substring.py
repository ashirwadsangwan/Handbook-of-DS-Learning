class Solution:
    def longestPalindrome(self, s: str) -> str:
        # base case
        if not s or not len(s):
            return ""

        max_str = ""

        max_length = 0

        # consider every character of the given string as a midpoint and expand in both directions to find the maximum length pallindrome

        for i in range(len(s)):

            # find the longest odd length pallindrome with `s[i]` as a midpoint

            curr_str = self.expand(s, i, i)
            curr_length = len(curr_str)

            # update maximum length pallindromic substring if the odd length palindrome has a greater length

            if curr_length > max_length:
                max_length = curr_length
                max_str = curr_str

            # find the longest even length pallindrome

            curr_str = self.expand(s, i, i + 1)
            curr_length = len(curr_str)

            # update maximum length pallindromic substring if the even length palindrome has a greater length

            if curr_length > max_length:
                max_length = curr_length
                max_str = curr_str

        return max_str

    def expand(self, s: str, low: int, high: int) -> str:
        length = len(s)

        # expand in both directions
        while low >= 0 and high < length and s[low] == s[high]:
            low -= 1
            high += 1

        return s[low + 1 : high]
