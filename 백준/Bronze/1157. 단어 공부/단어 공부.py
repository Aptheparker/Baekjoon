S = input().upper()
S_list = list(set(S))
l1 = []

for i in S_list:
  l1.append(S.count(i))

maxNum = max(l1)
indexNum = l1.index(maxNum)

if l1.count(maxNum) > 1:
  print('?')
  exit(0)

print(S_list[indexNum])