n = int(input())

numbers = map(int, input().split())

count = 0

for i in numbers:
  if i == n:
    count+=1

print(count)