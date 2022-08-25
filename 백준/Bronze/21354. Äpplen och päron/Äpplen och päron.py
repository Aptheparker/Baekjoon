a,b = map(int, input().split())

pa = 7*a
pb = 13*b

if pa<pb:
  print('Petra')
elif pa==pb:
  print('lika')
else:
  print('Axel')