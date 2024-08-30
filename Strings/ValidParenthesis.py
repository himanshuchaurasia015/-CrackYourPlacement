class Solution:
    def isValid(self, s):
        stack=[]
        d={"}":"{",")":"(","]":"["}
        for i in s:
            if i in d.values():
                stack.append(i)
            elif (not stack) or d[i]!=stack[-1]:
                return False
            else:
                stack.pop()
        if stack:
            return False
        return True