a, b = map(int, input().split())
if a > b:
  output = '>'
elif a < b:
  output = '<'
else:
  output = '=='

print(output)

