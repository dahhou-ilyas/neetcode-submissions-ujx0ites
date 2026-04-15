class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs[0])==0:
            return ""
        indexPointer = 0
        firsChar = strs[0][indexPointer]
        result = ""
        isNotPrefix = True
        while isNotPrefix : 
            for s in strs:
                if indexPointer < len(s) and s[indexPointer] != firsChar:
                    isNotPrefix = False
                    break
                if indexPointer >= len(s):
                    isNotPrefix = False
                    break
            if not isNotPrefix:
                break
            result += firsChar
            indexPointer += 1
            if indexPointer >= len(strs[0]):
                break
            firsChar = strs[0][indexPointer]

        return result

        