a = []

n = int(input())

for i in range(n):
  a.append(str(i+1) + ". " + input())

for i in range(n):
  print(a[i])