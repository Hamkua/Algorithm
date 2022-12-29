class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while (left < right):
            if (s[left].isalnum()):

                if (s[right].isalnum()):

                    if (s[left].upper() != s[right].upper()):
                        return False

                    right -= 1
                    left += 1
                    
                else:
                    right -= 1

            else:
                left += 1
        return True