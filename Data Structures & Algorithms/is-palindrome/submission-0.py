class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in s:
            if i.isalnum() == True:
                ans += i.lower()

        n = len(ans)
        for i in range(len(ans)):
            if ans[i] != ans[n-i-1]:
                return False
                break
        return True

        