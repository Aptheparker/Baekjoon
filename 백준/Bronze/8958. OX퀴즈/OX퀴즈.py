#input
T = int(input())



for i in range(1, T+1):
  plus = 0
  score = 0
  check = list(input())

#control
  for j in range(0, len(check)):
    if check[j] == 'O':
      plus += 1
      score += plus
    else:
      plus = 0
      
#output
  print(score)