class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0]) + 1):
            current = strs[0][:i]

            for s in strs:
                if s[:i] != current:
                    return prefix

            prefix = current

        return prefix