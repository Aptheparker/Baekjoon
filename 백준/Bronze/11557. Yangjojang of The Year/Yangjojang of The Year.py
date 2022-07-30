T = int(input())
l1 = []
l2 = []

for i in range(T):
  num = int(input())
    
  for i in range(num):
    y, k = map(str, input().split())
    l1.append(y)
    l2.append(int(k))
  

  print(l1[l2.index(max(l2))])