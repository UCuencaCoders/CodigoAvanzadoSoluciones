class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []

        for ele in tokens:
            if ele == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif ele == "-":
                stack.append(-(stack.pop() - stack.pop()))
            elif ele == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            elif ele == "*":
                stack.append(stack.pop()*stack.pop())
            else:
                stack.append(int(ele))

        return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Solution = Solution()
print(Solution.evalRPN(tokens)) 