class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(i):
            res = ""
            num = 0

            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])

                elif s[i] == '[':
                    sub, i = dfs(i + 1) 
                    res += sub * num
                    num = 0

                elif s[i] == ']':
                    return res, i

                else:
                    res += s[i]

                i += 1

            return res, i

        result, _ = dfs(0)
        return result