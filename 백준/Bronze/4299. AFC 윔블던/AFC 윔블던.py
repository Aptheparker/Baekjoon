a,b = map(int, input().split())


for i in range(1001):
  for j in range(1001):
    if i+j==a and (i-j==b or j-i==b):
      if i>=j:
        print(i,j)
        exit(0)
      else:
        print(j,i)
        exit(0)
    continue

print(-1)