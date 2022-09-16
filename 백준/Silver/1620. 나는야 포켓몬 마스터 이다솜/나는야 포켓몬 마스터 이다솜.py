#1620
import sys

a=[]

N,M = map(int, sys.stdin.readline().split())

for i in range(N):
  a.append(sys.stdin.readline().rstrip())

for j in range(M):
  get = sys.stdin.readline().rstrip()
  if get.isnumeric():
    print(a[int(get)-1])
  else:
    print(a.index(get)+1)
