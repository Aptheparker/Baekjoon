while True:
  a = input()
  if a == '0':
    exit(0)
  elif a[::-1] == a:
    print('yes')
  else:
    print('no')