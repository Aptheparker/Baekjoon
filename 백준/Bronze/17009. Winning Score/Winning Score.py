A1 = int(input())
A2 = int(input())
A3 = int(input())
B1 = int(input())
B2 = int(input())
B3 = int(input())

A = 3*A1+2*A2+A3
B = 3*B1+2*B2+B3

if A > B:
  print('A')
elif B > A:
  print('B')
else:
  print('T')