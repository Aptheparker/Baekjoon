T = int(input())
a = []

for i in range(T):
  num = int(input())
  if num == 0:
    a.pop()
  else:
    a.append(num)

print(sum(a))