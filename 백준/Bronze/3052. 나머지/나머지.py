l1 = []
l2 = []
count = 0

for i in range(10):
  l1.append(int(input()))
  l1[i] = l1[i] % 42
  l2 = list(set(l1))

print(len(l2))
