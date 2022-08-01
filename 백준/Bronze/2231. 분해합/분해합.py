num = int(input())

for i in range(num):
  total = 0

  for j in str(i):
    total += int(j)
  check = i + total
  if check == num:
    print(i)
    exit(0)

print(0)