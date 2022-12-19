a = int(input())
l1 = list(map(int, input().split()))
sum = 0
bonus=0
for number in l1:
  if number==1:
    bonus+=1
  else:
    bonus=0
  sum+=bonus

print(sum)