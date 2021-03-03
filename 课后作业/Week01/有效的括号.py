"""
有效的括号
"""


# 1
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack


# 2
class Solution:
    def isValid(self, s: str) -> bool:
        dic, stack = {")": "(", "]": "[", "}": "{"}, []
        for char in s:
            if stack and char in dic:
                if stack[-1] == dic[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack


# 3
class Solution:
    def isValid(self, s: str) -> bool:
        stack, dic = [], {")": "(", "]": "[", "}": "{"}
        for char in s:
            if stack and char in dic:
                if dic[char] == stack[-1]: stack.pop()
                else: return False
            else: stack.append(char)
        return not stack
