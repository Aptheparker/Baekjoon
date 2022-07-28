import math

T = int(input())

for i in range(T):
    numbers = list(map(int, input().split()))
    print(math.lcm(numbers[0], numbers[1]))