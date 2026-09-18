class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = "".join(c for c in s.lower() if c.isalnum())
        if len(normalized) < 2:
            return True
        half_length = len(normalized) // 2
        return normalized[:half_length] == "".join(reversed(normalized[-half_length:]))