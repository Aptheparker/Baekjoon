import sys

def empty(lst):
  if len(lst)==0:
    return 1
  else:
    return 0

n=int(sys.stdin.readline())
lst=[]

for i in range(n):
  a=list(sys.stdin.readline().split())
  if(a[0]=='push_front'):
    lst.insert(0,int(a[1]))
  elif(a[0]=='push_back'):
    lst.append(int(a[1]))
  elif(a[0]=='pop_front'):
    if empty(lst)==1:
      print(-1)
    else:
      print(lst[0])
      lst.pop(0)
  elif(a[0]=='pop_back'):
    if empty(lst)==1:
      print(-1)
    else:
      print(lst[-1])
      lst.pop()
  elif(a[0]=='size'):
    print(len(lst))
  elif(a[0]=='empty'):
    print(empty(lst))
  elif(a[0]=='front'):
    if empty(lst)==1:
      print(-1)
    else:
      print(lst[0])
  elif(a[0]=='back'):
    if empty(lst)==1:
      print(-1)
    else:
      print(lst[-1])