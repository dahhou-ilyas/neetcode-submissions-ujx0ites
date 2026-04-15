class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur = ""
        i = 0 
        reference = strs[0]

        if len(reference)==0:
            return ""
        if len(strs) == 1 :
            return reference

        for i, ch in enumerate(reference):
            for word in strs[1:]:
                if i >= len(word) or word[i] != ch:
                    return cur
            cur += ch
        return cur
