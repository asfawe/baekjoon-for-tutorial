# 힌트 Case #1:

number = int(input())

for i in range(1, number + 1):
    number1, number2 = map(int, input().split())
    print(f"Case #{i}: {number1 + number2}")
