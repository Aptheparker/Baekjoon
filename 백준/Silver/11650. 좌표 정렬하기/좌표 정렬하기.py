T = int(input())
l1 = []

for i in range(T):
  [x, y] = list(map(int, input().split()))
  l1.append([x, y])

l1.sort()

for i in range(T):
  print(l1[i][0], l1[i][1])