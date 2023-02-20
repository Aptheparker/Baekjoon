a=int(input())
lst=[]

for i in range(a):
  row,col=map(int,input().split())
  lst.append([row,col])


for i in lst:
  for j in range(i[1]):
    print('X'*i[0])
  print()