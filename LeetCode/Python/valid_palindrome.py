import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all non-alphanumeric characters using regex
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        if s == s[::-1]:
            return True
        else:
            return False