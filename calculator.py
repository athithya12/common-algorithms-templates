def calculate(s: str) -> int:
    it = 0

    def calc() -> int:
        nonlocal it

        def update(op: str, v: int) -> None:
            if op == "+":
                stack.append(v)
            if op == "-":
                stack.append(-v)
            if op == "*":
                stack.append(stack.pop() * v)
            if op == "/":
                stack.append(int(stack.pop() / v))

        num, stack, sign = 0, [], "+"

        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] in "+-*/":
                update(sign, num)
                num, sign = 0, s[it]
            elif s[it] == "(":
                it += 1
                num = calc()
            elif s[it] == ")":
                update(sign, num)
                return sum(stack)
            it += 1
        update(sign, num)
        return sum(stack)

    return calc()
