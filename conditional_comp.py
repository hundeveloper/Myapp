numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


result = []


# result = [x ** 2 if x % 2 == 0 else x for x in numbers]
for x in numbers:
    if x % 2 == 0:
        result.append(x ** 2)  # 짝수는 제곱
    else:
        result.append(x)  # 홀수는 그대로

print(result)
print(result)