class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(i):
            if i >= len(s) // 2:
                return
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
            helper(i + 1)
        helper(0)