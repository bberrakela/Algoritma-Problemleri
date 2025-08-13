class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        
        for i in range(1, len(strs)):
            while strs[i].startswith(prefix) == False:
                prefix = prefix[0:len(prefix)-1]
                if not prefix:
                    return ""
        
        return prefix
