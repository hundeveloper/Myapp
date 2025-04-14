def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b

if __name__ == "__main__":
    result = []
    i = 1
    while i <= 5:
        result.append(calculator(i, i, '*'))
        i += 1
    print(result)