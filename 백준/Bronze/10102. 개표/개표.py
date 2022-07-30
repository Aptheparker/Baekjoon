#input
T = int(input())
vote = input()

#control
A = 0
B = 0
for i in range(0, T):
  if vote[i] == 'A':
    A += 1
  elif vote[i] == 'B':
    B += 1

#output
if A > B:
  print('A')
elif B > A:
  print('B')
else: 
  print('Tie')
