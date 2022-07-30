#input
word = list(input())

#control
if word == word[::-1]:
  output = 1
else:
  output = 0

#output
print(output)
