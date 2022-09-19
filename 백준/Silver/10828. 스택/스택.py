import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
  K = sys.stdin.readline().split()

  if K[0]=='push':
    stack.append(K[1])
  elif K[0]=='pop':
    if not stack:
      print(-1)
    else:
      print(stack.pop())
  elif K[0]=='size':
    print(len(stack))
  elif K[0]=='top':
    if not stack:
      print(-1)
    else:
      print(stack[-1])
  elif K[0]=='empty':
    if not stack:
      print(1)
    else:
      print(0)