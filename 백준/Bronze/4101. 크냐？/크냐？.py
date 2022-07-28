a=1
b=1

while True:
  a, b = map(int, input().split())
  if a>b:
    print('Yes')
  elif a==0 and b==0:
    exit(0)
  elif a<=b:
    print('No')