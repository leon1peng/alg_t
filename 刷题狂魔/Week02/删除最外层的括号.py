"""
删除最外层的括号
"""


# 1
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result, stack = "", []
        for char in S:
            if char == "(":
                if stack:
                    result += char
                stack.append(char)
            if char == ")":
                stack.pop()
                if stack:
                    result += char
        return result


# 2
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result, stack = "", []
        for char in S:
            if char == "(":
                if stack:
                    result += char
                stack.append(char)
            if char == ")":
                stack.pop()
                if stack:
                    result += char
        return result


# 3
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, stack = "", []
        for char in S:
            if char == "(":
                if stack:
                    res += char
                stack.append(char)
            if char == ")":
                stack.pop()
                if stack:
                    res += char
        return res


# 4
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result, stack = "", list()
        for char in S:
            if char == "(":
                if stack:
                    result += char
                stack.append(char)
            if char == ")":
                stack.pop()
                if stack:
                    result += char
        return result


# 5
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result, stack = '', []
        for char in S:
            if char == "(":
                if stack:
                    result += char
                stack.append(char)
            if char == ")":
                stack.pop()
                if stack:
                    result += char
        return result
