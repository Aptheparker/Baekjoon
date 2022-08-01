num = int(input())
count = 0

for i in range(num):
  num -= 6 * i
  count += 1
  if num <= 1:
    break

print(count)