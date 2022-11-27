l1=[]

for i in range(7):
  n=int(input())

  if n%2==1:
    l1.append(n) 
  else:
    continue

if len(l1)==0:
  print(-1)
else:
  print(sum(l1))
  print(min(l1))