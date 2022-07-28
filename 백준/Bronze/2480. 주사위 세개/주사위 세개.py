a, b, c = map(int, input().split())


if (a != b and a != c) and (b != a and b != c) and (c != b and c != a):
  if a < b < c or b < a < c:
    res = c
  elif a < c < b or c < a < b:
    res = b
  elif b < c < a or c < b < a:
    res = a
  print(res * 100)
  
if a != b == c or  a != c == b or a == b != c or a == c != b:
  if a == b:
    res = a
  elif b == c:
    res = b
  elif a == c:
    res = c
  print(1000 + res * 100)

if a == b == c:
  res = a
  print(10000 + res * 1000) 