A,B = map(int, input().split())

C = int(input())

total = A + B

if total >= 2*C:
  print(total - 2*C)
else:
  print(total)