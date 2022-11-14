import re

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        numbers = []

        while tokens:
            token = tokens.pop(0)
            if re.match("-?\\d+", token):
                numbers.append(int(token))
            else:
                a = numbers.pop()
                b = numbers.pop()
                if token == "+":
                    numbers.append(b + a)
                elif token == "-":
                    numbers.append(b - a)
                elif token == "*":
                    numbers.append(b * a)
                elif token == "/":
                    numbers.append(int(b / a))

        return numbers[0]

if __name__ == "__main__":
    assert(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22)
    assert(Solution().evalRPN(["2","1","+","3","*"]) == 9)

