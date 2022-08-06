T = int(input())
a = []

for i in range(T):
  a.append(int(input()))

a.sort()

for i in range(T):
  print(a[i])