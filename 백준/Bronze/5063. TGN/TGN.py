#input
T = int(input())

#control
for i in range(1, T+1):
  r, e, c = map(int, input().split())
  profit = e - c
  if profit > r:
    output = 'advertise'
  elif profit == r:
    output = 'does not matter'
  else:
    output = 'do not advertise'
#output
  print(output)