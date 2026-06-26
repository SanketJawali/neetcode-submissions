class Solution:
    stack = []
    ops = ['+', '-', '*', '/']

    def evalRPN(self, tokens: List[str]) -> int:
        # for an int, push it to the stack
        # for any operator, pop 2 ints from stack and perform operation on them
        # result of any operation is also pushed to stack
        for token in tokens:
            if token in self.ops:
                b = self.stack.pop()
                a = self.stack.pop()
                # print(f"a: {a}, b: {b}, op: {token}")
                
                if token == self.ops[0]:
                    self.stack.append(a + b)
                elif token == self.ops[1]:
                    self.stack.append(a - b)
                elif token == self.ops[2]:
                    self.stack.append(a * b)
                elif token == self.ops[3]:
                    self.stack.append(int(a / b))
            else:
                self.stack.append(int(token))

        return self.stack.pop()