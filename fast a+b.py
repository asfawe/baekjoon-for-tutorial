import sys

number1 = int(sys.stdin.readline())

for i in range(number1):
    sum, sum2 = map(int, sys.stdin.readline().split())
    print(sum + sum2)
