T = 9
a = []

#input
for i in range(T):
  a.append(int(input()))

#control
  maxNum = max(a)
  maxIndex = a.index(max(a)) + 1

#output
print(maxNum)
print(maxIndex)