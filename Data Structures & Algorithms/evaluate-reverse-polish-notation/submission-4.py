class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:
            if token == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                ans = n2 + n1
                stack.append(ans)
            elif token == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                ans = n2 - n1
                stack.append(ans)
            elif token == "*":
                n1 = stack.pop()
                n2 = stack.pop()
                ans = n2 * n1
                stack.append(ans)
            elif token == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                ans = int(n2 / n1)
                stack.append(ans)
            else:
                temp = int(token)
                stack.append(temp)
                
            
        return stack[-1]