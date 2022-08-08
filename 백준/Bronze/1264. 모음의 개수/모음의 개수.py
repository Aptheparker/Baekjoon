while True:
  S = input()
  if S == '#':
    break
  
  else:
    count = 0
    for i in S:
      if i in 'aeiouAEIOU':
        count += 1

  print(count)