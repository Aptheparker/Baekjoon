while True:
#input
  M, F = map(int, input().split())

#control
  if M == 0 and F == 0:
    exit(0)
  else: 
    total = M + F

#output
  print(total)