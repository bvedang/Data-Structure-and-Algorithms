class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "*":
                val2 = stack.pop()
                val1 = stack.pop()
                res = val1 * val2
                stack.append(int(res))
            elif token == "/":
                val2 = stack.pop()
                val1 = stack.pop()
                res = val1 / val2 
                stack.append(int(res))
            elif token == "+":
                val2 = stack.pop()
                val1 = stack.pop()
                res = val1 + val2
                stack.append(int(res))
            elif token == "-":
                val2 = stack.pop()
                val1 = stack.pop()
                res = val1 - val2
                stack.append(int(res))
            else:
                stack.append(int(token))
        return stack[-1]