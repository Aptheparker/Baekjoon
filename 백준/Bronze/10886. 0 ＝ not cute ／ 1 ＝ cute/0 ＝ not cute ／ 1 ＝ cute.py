#input
T = int(input())

#control

cute = 0
notcute = 0
for i in range(0, T):
  vote = int(input())
  if vote == 1:
    cute += 1
  elif vote == 0:
    notcute += 1
#output
if cute > notcute:
  print('Junhee is cute!')
elif notcute > cute:
  print('Junhee is not cute!')
