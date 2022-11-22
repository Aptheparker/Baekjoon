a = int(input())

for i in range(a):
  print(i*' ', end='')
  print((2*a - (2*i+1)) * '*')

for i in range(2,a+1):
  print((a-i)*' ', end='')
  print((2*i-1) * '*')