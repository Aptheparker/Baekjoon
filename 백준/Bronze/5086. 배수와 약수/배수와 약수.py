while True:
#input
  a, b = map(int, input().split())

#control
  if a == 0 and b == 0:
    exit(0)
  elif b % a == 0:
    output = 'factor'
  elif a % b == 0:
    output = 'multiple'
  else:
    output = 'neither'

#output
  print(output)