class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase
        ls = s.lower()
        
        l = 0
        r = len(ls) - 1

        while l <= r:
            # Skip non-alphanumeric characters from the left
            while l < r and not ls[l].isalnum():
                l += 1
            # Skip non-alphanumeric characters from the right
            while r > l and not ls[r].isalnum():
                r -= 1

            # Compare the characters
            if ls[l] != ls[r]:
                return False

            # Move towards the middle
            l += 1
            r -= 1

        return True