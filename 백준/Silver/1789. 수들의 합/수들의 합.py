a = int(input())
s = 0
count = 0

for i in range(1, a+1):
  s += i
  count += 1
  if s > a:
    count -= 1
    break
  elif s == a:
    break

print(count)