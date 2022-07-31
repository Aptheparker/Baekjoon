#input
num = int(input())


#control
for i in range(num):
  output = ((num-(i+1)) * ' ') + ((i+1)*'*')

#output
  print(output)